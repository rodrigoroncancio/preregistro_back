
from decimal import Decimal
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from core.azure import upload_file, descargar_archivo
import hashlib, os
   
class ArchivoViewSet(viewsets.GenericViewSet):
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [StaffPermission]
    permission_classes = []

    def ruta_archivo(self, entrega_id, filename):
        subcarpeta = "a" + str(entrega_id)
        extension = os.path.splitext(filename)[1]
        md5_hash = hashlib.md5(filename.encode()).hexdigest()
        return "acuerdo/" + subcarpeta + "/" + md5_hash + extension

    def subir(self, request, *args, **kwargs):
        dataReq = request.data
        if "tipo" not in dataReq:
            return Response({"error": "Tipo no encontrado"}, status=status.HTTP_400_BAD_REQUEST)
        if dataReq["tipo"] not in ("prueba", "acuerdo", "legalizacion"):
            return Response({"error": "Tipo no encontrado"}, status=status.HTTP_400_BAD_REQUEST)
        acuerdo = int(kwargs["acuerdo"])
        if acuerdo > 0 :
            instance = Acuerdo.objects.filter(id=acuerdo).first()
            if instance is None:
                return Response({"error": "Acuerdo no encontrado"}, status=status.HTTP_400_BAD_REQUEST)
            file_obj = request.FILES.get('archivo')
            if not file_obj or file_obj.content_type != 'application/pdf':
                return Response({"error": "Por favor, suba un archivo PDF válido."}, status=status.HTTP_400_BAD_REQUEST)
            destino = self.ruta_archivo(instance.id, file_obj.name)
            ruta = upload_file(file_obj, destino)
            if ruta == "":
                return Response({"error": "No se pudo subir el archivo"}, status=status.HTTP_400_BAD_REQUEST)                
            if "acuerdo" == dataReq["tipo"]:
                instance.ruta_acuerdo = ruta
            elif "legalizacion" == dataReq["tipo"]:
                instance.ruta_legalizacion = ruta
                instance.con_legalizacion = True
            else:
                # pass
                instance.ruta_acuerdo = ruta
            instance.save()
            return Response({"mensaje": "Archivo subido exitosamente."}, status=status.HTTP_201_CREATED)
        else :
            return Response({"error": "Debe incluir el id de acuerdo"}, status=status.HTTP_400_BAD_REQUEST)
        
    def descargar(self, request, *args, **kwargs):
        contenido = descargar_archivo("1000046724-13_20_4.jpg")
        if contenido is None:
            return Response({"error": "No se pudo descargar el archivo o no existe"}, status=status.HTTP_400_BAD_REQUEST)
        response = HttpResponse(contenido, content_type='application/image')
        response['Content-Disposition'] = f'attachment; filename=dd.jpg'
        return response
