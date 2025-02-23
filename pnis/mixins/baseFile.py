import os
import uuid
import base64
from rest_framework import serializers
from django.core.files.base import ContentFile

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
        file_fields = [field for field in data.keys() if field.startswith('url_')]

        for field in file_fields:
            if field in data:
                base64_content = data.pop(field)
                original_field = field.replace('url_', '')

                if base64_content:
                    # Si ya hay un archivo existente y coincide, lo mantenemos
                    if (original_field in data and
                        data[original_field] and
                        data[original_field] != "" and
                        data[original_field] in base64_content):
                        continue

                    # Guardamos el nuevo archivo
                    new_file = self.save_file(base64_content)
                    if new_file:
                        data[original_field] = new_file
                else:
                    # Si el base64 está vacío, limpiamos el campo
                    if original_field in data:
                        data[original_field] = ""

        return data

    def save_file(self, base64_string):
        try:
            # Separar el formato y el contenido
            format_part, file_content = base64_string.split(';base64,')
            file_type = format_part.split('data:')[1]

            # Determinar la extensión根据el tipo MIME
            extension_map = {
                'image/jpeg': '.jpg',
                'image/png': '.png',
                'application/pdf': '.pdf',
                'text/plain': '.txt',
                # Agrega más tipos MIME según necesites
            }
            extension = extension_map.get(file_type, '.bin')  # .bin como fallback

            # Generar nombre único para el archivo
            filename = f"{uuid.uuid4()}{extension}"
            directory = os.path.join('media', 'uploads')  # Puedes personalizar el directorio
            file_path = os.path.join(directory, filename)

            # Crear directorio si no existe
            os.makedirs(directory, exist_ok=True)

            # Guardar el archivo
            with open(file_path, 'wb') as f:
                f.write(base64.b64decode(file_content))

            return file_path
        except Exception as e:
            print(f"Error saving file: {e}")
            return None