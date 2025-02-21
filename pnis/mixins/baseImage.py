import os
import uuid
import base64
import hashlib
from rest_framework import serializers
from django.core.files.base import ContentFile

class BaseImageMixin:
    url_image = serializers.CharField(write_only=True, required=False, allow_blank=True)

    def validate(self, data):
        if 'url_image' in data:
            base64_img = data.pop('url_image')
            if base64_img:
                if 'image' in data and data['image'] and data['image'] != "" and data['image'] in base64_img:
                    pass
                else:
                    new_image = self.save_image(base64_img)
                    if new_image:
                        data['image'] = new_image
            else:
                if 'image' in data:
                    data['image'] = ""
        return data


    def save_image(self, base64_img):
        try:
            format, imgstr = base64_img.split(';base64,')

            filename = str(uuid.uuid4()) + '.jpg'
            directory = os.path.join('media')
            file_path = os.path.join(directory, filename)

            os.makedirs(directory, exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(base64.b64decode(imgstr))

            return file_path
        except Exception as e:
            print(f"Error saving image: {e}")
            return None
