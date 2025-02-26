from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.azure import descargar_archivo
import hashlib
import filetype
import os

class ArchivoKeyViewSet(viewsets.GenericViewSet):
 
    def generar(self, request, *args, **kwargs):
        usuario = request.user.username
        priv_key = settings.SECRET_KEY
        if not usuario or not priv_key:
            return Response({"error": "No se pudo generar la clave"}, status=status.HTTP_400_BAD_REQUEST)
        hash_md5 = hashlib.md5()
        hash_md5.update(f'{usuario}:{priv_key}'.encode('utf-8'))
        return Response(hash_md5.hexdigest(), status=status.HTTP_200_OK)

class ArchivoViewSet(viewsets.GenericViewSet):
    # parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
 
    def descargar(self, request, *args, **kwargs):
        key = kwargs.pop('key', None)
        uid = kwargs.pop('uid', 0)
        if not key or not uid:
            return Response({"error": "Petición incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
        user = get_user_model().objects.filter(id=uid).first()
        priv_key = settings.SECRET_KEY
        if user is None or not priv_key:
            return Response({"error": "Petición con datos errados"}, status=status.HTTP_400_BAD_REQUEST)
        hash_md5 = hashlib.md5()
        hash_md5.update(f'{user.username}:{priv_key}'.encode('utf-8'))
        if hash_md5.hexdigest()!= key:
            return Response({"error": "Clave incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)

        ruta = request.GET.get('ruta','')
        if ruta:
            ruta_sin_extension, extension = os.path.splitext(ruta)
            if extension.lower() in [".heif", ".heic"]:
                ruta = ruta_sin_extension + ".jpg"
            contenido = descargar_archivo(ruta)
            if contenido is None:
                return Response({"error": "No se pudo descargar el archivo o no existe"}, status=status.HTTP_404_NOT_FOUND)
            kind = filetype.guess(contenido)
            if kind is not None:
                content_type = kind.mime
            else:
                content_type = 'application/octet-stream'
            nombre_archivo = ruta.split("/")[-1]
            response = HttpResponse(contenido, content_type=content_type)
            response['Content-Disposition'] = f'attachment; filename={nombre_archivo}'
            return response
   