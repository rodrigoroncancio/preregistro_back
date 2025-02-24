from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.azure import descargar_archivo

class ArchivoViewSet(viewsets.GenericViewSet):
    # parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
 
    def descargar(self, request, *args, **kwargs):
        ruta = request.GET.get('ruta','')
        if ruta:
            contenido = descargar_archivo(ruta)
            if contenido is None:
                return Response({"error": "No se pudo descargar el archivo o no existe"}, status=status.HTTP_400_BAD_REQUEST)
            response = HttpResponse(contenido, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename=prueba.pdf'
            return response
   