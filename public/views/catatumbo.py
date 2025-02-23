from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import FormCatatumboPreregistro, FormCatatumboPreinscripcionDesplazados, FormCatatumboPreinscripcionGrupoProductores, FormCatatumboPreinscripcionNucleo

from ..serializers.catatumbo_preregistro import CatatumboPreregistroSerializer
from ..serializers.catatumbo_preinscripcionnucleo import CatatumboPreincripcionNucleoSerializer
from ..serializers.catatumbo_preinscripciondesplazados import CatatumboPreincripcionDesplazadosSerializer
from ..serializers.catatumbo_preinscripciongrupoproductores import CatatumboPreincripcionGrupoProductoresSerializer
from ..serializers.catatumbo_preinscripcionnucleosindividuales import CatatumboPreincripcionNucleosIndividualesSerializer
from ..serializers.catatumbo_preinscripcionfamiliaspnis import CatatumboPreincripcionFamiliasPnisSerializer

class CatatumboPreregistroView(APIView):

    def post(self, request):
        serializer = CatatumboPreregistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatatumboPreinscripcionNucleoView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionNucleoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatatumboPreinscripcionDesplazdosView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionDesplazadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CatatumboValidaDocumentoView(APIView):
    def get(self, request):
        documento = request.query_params.get('documento')
        
        # Verificar en la primera base de datos
        if FormCatatumboPreregistro.objects.filter(numero_documento=documento).exists():
            return Response(True, status=status.HTTP_200_OK)
        
        # Verificar en la segunda base de datos
        if FormCatatumboPreinscripcionDesplazados.objects.filter(numero_documento=documento).exists():
            return Response(True, status=status.HTTP_200_OK)
        
        # Verificar en la tercera base de datos
        if FormCatatumboPreinscripcionGrupoProductores.objects.filter(lider_identificacion=documento).exists():
            return Response(True, status=status.HTTP_200_OK)
        
        # Verificar en la cuarta base de datos
        if FormCatatumboPreinscripcionNucleo.objects.filter(numero_documento=documento).exists():
            return Response(True, status=status.HTTP_200_OK)
        
        return Response(False, status=status.HTTP_200_OK)

    
class CatatumboPreinscripcionGrupoProductoresView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionGrupoProductoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CatatumboPreinscripcionNucleosIndividualesView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionNucleosIndividualesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CatatumboPreinscripcionFamiliasPnisView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionFamiliasPnisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
