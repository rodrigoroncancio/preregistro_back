from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from core.models import PersonaPnis,  ArgeliaPersonas, ArgeliaPersonasValidadas, CatatumboPersonasValidadas, VCatatumboIndividuales
from core.serializers.staff import ArgeliaPersonasSerializer
from core.serializers.catatumbo import CatatumboIndividualSerializer
from ..models import VArgelia2IndividualValidaciones, VCatatumboIndividualValidaciones, FormCatatumbosFichaAcuerdo,FormCatatumnoFichaAcuerdoNucleoFamiliar, FormCatatumboPreregistro, FormCatatumboPreinscripcionDesplazados, FormCatatumboPreinscripcionGrupoProductores, FormCatatumboPreinscripcionNucleo, FormArgeliaFichaAcuerdo

from ..serializers.catatumbo_preregistro import CatatumboPreregistroSerializer
from ..serializers.catatumbo_preinscripcionnucleo import CatatumboPreincripcionNucleoSerializer
from ..serializers.catatumbo_preinscripciondesplazados import CatatumboPreincripcionDesplazadosSerializer
from ..serializers.catatumbo_preinscripciongrupoproductores import CatatumboPreincripcionGrupoProductoresSerializer
from ..serializers.catatumbo_preinscripcionnucleosindividuales import CatatumboPreincripcionNucleosIndividualesSerializer
from ..serializers.catatumbo_preinscripcionfamiliaspnis import CatatumboPreincripcionFamiliasPnisSerializer
from ..serializers.argelia_fichaacuerdo import ArgeliaFichaAcuerdoSerializer, FormArgeliaFichaAcuerdoNucleoFamiliarSerializer
from ..serializers.catatumbo_fichaacuerdo import CatatumboFichaAcuerdoSerializer, FormCatatumboFichaAcuerdoNucleoFamiliarSerializer

class CatatumboPreregistroView(APIView):

    def post(self, request):
        serializer = CatatumboPreregistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class CatatumboPreinscripcionNucleoView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionNucleoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class CatatumboPreinscripcionDesplazdosView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionDesplazadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class ConsultarDocumentoView(viewsets.GenericViewSet):
    # authentication_classes = [SessionAuthentication]
    permission_classes = []
    
    def consultar(self, request, doc, fecha):
        # Obtener los parámetros del cuerpo de la solicitud
        documento = doc
        fecha_nacimiento = fecha

        # Verificar si ambos campos están presentes
        if not documento or not fecha_nacimiento:
            return Response({'detail': 'Los campos "numdocumento" y "fechanacimiento" son obligatorios.'}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # Buscar en la primera base de datos
        resultado1 = VArgelia2IndividualValidaciones.objects.filter(identificacion=documento, fecha_nacimiento=fecha_nacimiento)
        if resultado1.exists():
            # Si hay resultados, devolver con status 1
            return Response({'status': 1, 'data': resultado1.values()}, status=status.HTTP_200_OK)

        # Buscar en la segunda base de datos
        resultado2 = VCatatumboIndividualValidaciones.objects.filter(identificacion=documento, fecha_nacimiento=fecha_nacimiento)
        if resultado2.exists():
            # Si hay resultados, devolver con status 1
            return Response({'status': 2, 'data': resultado2.values()}, status=status.HTTP_200_OK)

        # Si no hay resultados en ambas bases de datos, devolver status 2
        return Response({'status': 3, 'data': []}, status=status.HTTP_200_OK)
    
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

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
    
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    
class CatatumboFichaValidaDocumentoView(APIView):
    permission_classes = []
    def get(self, request):
        documento = request.query_params.get('documento')
        if not(PersonaPnis.objects.filter(identificacion=int(documento)).exists()):  
            return Response(
                {
                    "status": 1,
                    "data": {}
                },
                status=status.HTTP_200_OK
            )   
        else:
            registro = PersonaPnis.objects.filter(identificacion=int(documento)).first()
            serializer = UserPNISSerializer(registro)
            return Response(
                {
                    "status": 1,
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
            
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
            
    
class CatatumboFichaValidaDocumentoView(APIView):
    permission_classes = []
    def get(self, request):
        documento = request.query_params.get('documento')
        if not(PersonaPnis.objects.filter(identificacion=int(documento)).exists()):
            if FormCatatumbosFichaAcuerdo.objects.filter(numero_identificacion=documento).exists():
                return Response(
                {
                    "status": 2,
                    "data": {}
                },
                status=status.HTTP_200_OK
            ) 

            if CatatumboPersonasValidadas.objects.filter(numero_identificacion=documento).exists():
            # Buscar si el documento existe
                registro = VCatatumboIndividuales.objects.filter(identificacion=documento).first()

                if registro:
                    # Serializar el registro encontrado
                    serializer = CatatumboIndividualSerializer(registro)
                    return Response(
                        {
                            "status": 1,
                            "data": serializer.data
                        },
                        status=status.HTTP_200_OK
                    )
                    # Si no existe, devolver estructura estándar con `success: false` y `data: {}`
                return Response(
                    {
                        "status": 3,
                        "data": {}
                    },
                    status=status.HTTP_200_OK
                )   

            # Si no existe, devolver estructura estándar con `success: false` y `data: {}`
            registro = VCatatumboIndividuales.objects.filter(identificacion=documento).first()
            if registro:
                return Response(
                {
                    "status": 4,
                    "data": {}
                },
                status=status.HTTP_200_OK
            )  
            else :
                return Response(
                {
                    "status": 3,
                    "data": {}
                },
                status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "status": 5,
                    "data": {}
                },
                status=status.HTTP_200_OK
            )  
            
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
            
class CatatumboFichaValidaNucleoView(APIView):
    permission_classes = []
    def get(self, request):
        documento = request.query_params.get('documento')
        if not(PersonaPnis.objects.filter(identificacion=int(documento)).exists()):
            
            if FormCatatumnoFichaAcuerdoNucleoFamiliar.objects.filter(numero_identificacion=documento).exists():
                return Response(
                {
                    "status": 5,
                    "data": {}
                },
                status=status.HTTP_200_OK
                )
            
            if FormCatatumbosFichaAcuerdo.objects.filter(numero_identificacion=documento).exists():
                return Response(
                {
                    "status": 2,
                    "data": {}
                },
                status=status.HTTP_200_OK
                ) 
            if CatatumboPersonasValidadas.objects.filter(numero_identificacion=documento).exists():
                return Response(
                {
                    "status": 3,
                    "data": {}
                },
                status=status.HTTP_200_OK
                ) 
            else:
                return Response(
                {
                    "status": 1,
                    "data": {}
                },
                status=status.HTTP_200_OK
                ) 
        else:
            return Response(
                {
                    "status": 4,
                    "data": {}
                },
                status=status.HTTP_200_OK
            )  
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass        
            
class CatatumboFichaAcuerdoNucleoView(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        # Pasamos los datos correctamente con el argumento `data=`
        serializer = FormCatatumboFichaAcuerdoNucleoFamiliarSerializer(data=request.data, many=True)

        if serializer.is_valid():
            personas = serializer.save()
            return Response({"message": "Personas creadas correctamente", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass         
    
class ArgeliaFichaValidaDocumentoView(APIView):
    permission_classes = []
    def get(self, request):
        documento = request.query_params.get('documento')
        
        if FormArgeliaFichaAcuerdo.objects.filter(numero_identificacion=documento).exists():
            return Response(
            {
                "status": 2,
                "data": {}
            },
            status=status.HTTP_200_OK
        ) 

        if ArgeliaPersonasValidadas.objects.filter(numero_identificacion=documento).exists():
        # Buscar si el documento existe
            registro = ArgeliaPersonas.objects.filter(identificacion=documento).first()

            if registro:
                # Serializar el registro encontrado
                serializer = ArgeliaPersonasSerializer(registro)
                return Response(
                    {
                        "status": 1,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
                # Si no existe, devolver estructura estándar con `success: false` y `data: {}`
            return Response(
                {
                    "status": 3,
                    "data": {}
                },
                status=status.HTTP_200_OK
            )   

        # Si no existe, devolver estructura estándar con `success: false` y `data: {}`
        registro = ArgeliaPersonas.objects.filter(identificacion=documento).first()
        if registro:
            return Response(
            {
                "status": 4,
                "data": {}
            },
            status=status.HTTP_200_OK
        )  
        else :
            return Response(
            {
                "status": 3,
                "data": {}
            },
            status=status.HTTP_200_OK)
            
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    
class ArgeliaFichaAcuerdoNucleoView(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        # Pasamos los datos correctamente con el argumento `data=`
        serializer = FormArgeliaFichaAcuerdoNucleoFamiliarSerializer(data=request.data, many=True)

        if serializer.is_valid():
            personas = serializer.save()
            return Response({"message": "Personas creadas correctamente", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class CatatumboPreinscripcionGrupoProductoresView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionGrupoProductoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class CatatumboPreinscripcionNucleosIndividualesView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionNucleosIndividualesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class CatatumboPreinscripcionFamiliasPnisView(APIView):

    def post(self, request):
        serializer = CatatumboPreincripcionFamiliasPnisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    
class ArgeliaFichaAcuerdoView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = ArgeliaFichaAcuerdoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    
class CatatumboFichaAcuerdoView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = CatatumboFichaAcuerdoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
