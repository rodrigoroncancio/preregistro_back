# import os
import uuid
import base64
from rest_framework import serializers
from core.azure import upload_file
from pillow_heif import register_heif_opener
from PIL import Image
from io import BytesIO

class BaseFileMixin:
    @staticmethod
    def base64_file():
        class FileFieldSerializer(serializers.CharField):
            def to_internal_value(self, data):
                if data and ';base64,' in data:
                    saved_file = BaseFileMixin.save_file(data)
                    if saved_file:
                        return saved_file
                return None

        return FileFieldSerializer(write_only=True, required=False, allow_blank=True)

    @staticmethod
    def save_file(base64_data, folder='validacion'):
        try:
            format_info, file_str = base64_data.split(';base64,')
            file_ext = format_info.split('/')[-1]
            contenido = base64.b64decode(file_str)
            if file_ext == 'heif':
                register_heif_opener()
                # Crear un objeto BytesIO para manejar los datos de la imagen
                image_stream = BytesIO(contenido)
                image = Image.open(image_stream)
                output_stream = BytesIO()
                # Guardar la imagen en formato JPG
                image.save(output_stream, format="JPEG", quality=80)
                contenido = output_stream.getvalue()
                file_ext = "jpg"

            filename = f"{uuid.uuid4()}.{file_ext}" 
            file_path = f'{folder}/{filename}'  # Aquí se guarda el archivo en la carpeta
            respuesta = upload_file(contenido, file_path)
            if respuesta == "":
                return None

            return file_path  # ruta relativa en el blob
        except Exception as e:
            print(f"Error saving file: {e}")
            return None
