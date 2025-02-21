from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import FormCatatumboPreregistro

from ..serializers.catatumbo_preregistro import CatatumboPreregistroSerializer

class CatatumboPreregistroView(APIView):

    def post(self, request):
        serializer = CatatumboPreregistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatatumboValidaDocumentoView(APIView):

    def get(self, request):
        documento = request.query_params.get('documento')

        # Completar esta logica
        existeDocumento = FormCatatumboPreregistro.objects.filter(numero_documento=documento).exists()
        return Response(existeDocumento, status=status.HTTP_200_OK)
