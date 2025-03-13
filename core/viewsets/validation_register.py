from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

from core.models import ValidationFinalRegister, ValidationRegister, ValidationItems, ValidationArgeliaPersonas, CedulasRnec
from core.serializers.validation_register import ValidationFinalRegisterSerializer, ValidationRegisterSerializer, ValidationRegisterLiteSerializer, ValidationPersonasSerializer, ValidationItemsSerializer, CedulasRnecSerializer

class CedulasRnecViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CedulasRnecSerializer
    queryset = CedulasRnec.objects.all()

    @action(detail=False, methods=['get'], url_path='getbyidentification/(?P<ide>\d+)')
    def get_by_identification(self, request, ide=None):

        cedula = CedulasRnec.objects.get(numero_cedula=int(ide))
        serializer = self.get_serializer(cedula)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ValidationFinalRegisterViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ValidationFinalRegisterSerializer
    queryset = ValidationFinalRegister.objects.all()   
    

class ValidationRegisterViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ValidationRegisterSerializer
    queryset = ValidationRegister.objects.all()
    
    @action(detail=True, methods=['delete'])
    def delete_by_id(self, request, pk=None):
        """Elimina un ValidationRegister por ID."""
        validation = get_object_or_404(ValidationRegister, pk=pk)
        validation.delete()
        return Response({"message": "Registro eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='missing-validation-items/(?P<document_number>[^/.]+)/(?P<survey_id>[^/.]+)')
    def missing_validation_items(self, request, document_number, survey_id):
        auth = request.auth
        array_roles = auth.payload["roles"]
        # Obtener los ValidationItems registrados en ValidationRegister con ese document_number y survey_id
        registered_items = ValidationRegister.objects.filter(
            document_number=document_number,
            SurveyForms_id=survey_id
        ).values_list('validationitems_id', flat=True)

        # Obtener los ValidationItems que no están registrados
        missing_items = ValidationItems.objects.filter(rol_id__in=array_roles, survey=survey_id, activated=True).exclude(id__in=registered_items)

        # Serializar los resultados
        return Response({"missing_items": list(missing_items.values())})

    @action(detail=False, methods=['get'], url_path='filterbydocumentnumber/(?P<document_number>[^/.]+)/(?P<survey_id>[^/.]+)/(?P<status>[^/.]+)')
    def filterbydocumentnumber(self, request, document_number, survey_id, status):
        if status == 'no':
            registered_items = ValidationRegister.objects.filter(
                document_number=document_number,
                SurveyForms_id=survey_id,
                status=status
            )
            serializer = ValidationRegisterLiteSerializer(registered_items, many=True)
            return Response(serializer.data)
        else:
            auth = request.auth
            array_roles = auth.payload["roles"]
            val_item = ValidationItems.objects.filter(rol_id__in=array_roles, survey=survey_id, activated=True)
            registered_items = ValidationRegister.objects.filter(
                document_number=document_number,
                SurveyForms_id=survey_id,
                validationitems__rol_id__in=array_roles
            )
            serializer = ValidationRegisterLiteSerializer(registered_items, many=True)
            data = serializer.data
            ids = {objeto["validationitems_id"] for objeto in data}
            for item in val_item:
                if item.id not in ids:
                    data.append({"id": None, "user_name": None, "status": "-", "observation": None, "attachment": None, "validationitems_id": item.id})
            return Response(data)
    
    @action(detail=False, methods=['get'], url_path='personas-validadas/argelia')
    def personas_validadas(self, request):
        validated_items = ValidationArgeliaPersonas.objects.all()
        search = request.GET.get('search[value]',"")
        if search != "":
            validated_items = validated_items.filter(
                Q(nombres__icontains=search) | Q(apellidos__icontains=search) | Q(numero_documento__icontains=search) | Q(corregimiento__icontains=search) | Q(vereda__icontains=search)
            )
        # Serializar los resultados
        serializer = ValidationPersonasSerializer(validated_items, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='items-validacion/(?P<survey_id>[^/.]+)')
    def item_validacion(self, request, *args, **kwargs):
        survey_id = int(kwargs['survey_id'])
        validation_items = ValidationItems.objects.filter(survey=survey_id, activated = True).order_by('rol')
        # Serializar los resultados
        serializer = ValidationItemsSerializer(validation_items, many=True)
        return Response(serializer.data)
