from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import ValidationItems, ValidationArgeliaPersonas
from core.serializers.staff import ValidationRegisterSerializer, ValidationRegisterLiteSerializer, ValidationRegister
from core.serializers.validation_register import ValidationPersonasSerializer

class ValidationRegisterViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ValidationRegisterSerializer
    queryset = ValidationRegister.objects.all()

    @action(detail=False, methods=['get'], url_path='missing-validation-items/<str:document_number>/<int:survey_id>')
    def missing_validation_items(self, request, document_number, survey_id):
        # Obtener los ValidationItems registrados en ValidationRegister con ese document_number y survey_id
        registered_items = ValidationRegister.objects.filter(
            document_number=document_number,
            SurveyForms_id=survey_id
        ).values_list('validationitems_id', flat=True)

        # Obtener los ValidationItems que no están registrados
        missing_items = ValidationItems.objects.filter(activated = True).exclude(id__in=registered_items)

        # Serializar los resultados
        return Response({"missing_items": list(missing_items.values())})

    # @action(detail=False, methods=['get'], url_path='filterbydocumentnumber/<str:document_number>/<int:survey_id>/<str:status>')
    def filterbydocumentnumber(self, request, document_number, survey_id, status):
        registered_items = ValidationRegister.objects.filter(
            document_number=document_number,
            SurveyForms_id=survey_id,
            status=status
        )

        # Usar el serializer ligero
        serializer = ValidationRegisterLiteSerializer(registered_items, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='personas-validadas/argelia')
    def personas_validadas(self, request):
        # Obtener los ValidationItems registrados en ValidationRegister con ese document_number y survey_id
        validated_items = ValidationArgeliaPersonas.objects.all()
        search = request.GET.get('search[value]',"")
        if search != "":
            validated_items = validated_items.filter(
                Q(nombres__icontains=search) | Q(apellidos__icontains=search) | Q(numero_documento__icontains=search) | Q(corregimiento__icontains=search) | Q(vereda__icontains=search)
            )
        # Serializar los resultados
        serializer = ValidationPersonasSerializer(validated_items, many=True)
        return Response(serializer.data)
