import os
import uuid
import base64
import re
import logging
from django.conf import settings
from django.db import models
from rest_framework import serializers

logger = logging.getLogger(__name__)

class BaseFileMixin:
    @classmethod
    def url_file(cls, field_name):
        return serializers.CharField(
            write_only=True,
            required=False,
            allow_blank=True,
            source=field_name
        )

    def validate(self, data):
        model_fields = [field.name for field in self.Meta.model._meta.fields]
        file_fields = [
            field_name for field_name, field in self.fields.items()
            if field.write_only and field.source in model_fields
        ]
        
        for field in file_fields:
            if field in data:
                base64_content = data.pop(field)
                original_field = self.fields[field].source

                if base64_content and ';base64,' in base64_content:
                    new_file = self.save_file(base64_content)
                    if new_file is not None:
                        data[original_field] = new_file
                    else:
                        raise serializers.ValidationError(f"Error guardando archivo en {original_field}")
                elif base64_content == "":
                    data[original_field] = ""

        return data

    def save_file(self, base64_string):
        try:
            match = re.match(r'data:(?P<mime>[^;]+);base64,(?P<data>.+)', base64_string)
            if not match:
                raise serializers.ValidationError("Formato base64 inválido")

            file_type = match.group("mime")
            file_content = match.group("data")

            extension_map = {
                'image/jpeg': '.jpg',
                'image/png': '.png',
                'application/pdf': '.pdf',
                'text/plain': '.txt',
            }
            extension = extension_map.get(file_type, '.bin')

            filename = f"{uuid.uuid4()}{extension}"
            directory = os.path.join(settings.MEDIA_ROOT, 'uploads')
            os.makedirs(directory, exist_ok=True)

            file_path = os.path.join(directory, filename)
            with open(file_path, 'wb') as f:
                f.write(base64.b64decode(file_content))

            return os.path.relpath(file_path, settings.MEDIA_ROOT)
        except Exception as e:
            logger.error(f"Error saving file: {e}")
            return None

# Modelo corregido
class Staff(models.Model):
    image = models.FileField(upload_to='uploads/', blank=True, null=True)
    foto_documento = models.FileField(upload_to='uploads/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Staff {self.phone}"

# Serializer corregido
class StaffInfoSerializer(BaseFileMixin, serializers.ModelSerializer):
    image = BaseFileMixin.url_file('image')
    foto_documento = BaseFileMixin.url_file('foto_documento')

    class Meta:
        model = Staff
        fields = '__all__'
