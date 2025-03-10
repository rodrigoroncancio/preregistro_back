from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAdminUser
from django.contrib.auth import get_user_model
from django.db.models import Count

from public.models import FormArgeliaFichaAcuerdo
from core.models import NucleoFamiliarPersonas, UserPNIS, Department, Municipality, Township, Village, ArgeliaGrupos, ArgeliaPersonas, ValidationRegister, ValidationItems, CatatumboIndividuales
from core.serializers.staff import NucleoFamiliarSerializer, StaffSerializer, StaffListSerializer, UserPNISSerializer, DepartmentSerializer, MunicipalitySerializer, TownshipSerializer, VillageSerializer, ArgeliaGruposSerializer, ArgeliaPersonasSerializer, FichaAcuerdoFase2Serializer
from core.serializers.catatumbo import CatatumboIndividualSerializer
from pnis.filters import ORFilterBackend

def setContext (context, formid):
    auth = context['request'].auth
    array_roles = auth.payload["roles"]
    total_item = ValidationItems.objects.filter(rol_id__in=array_roles, survey=formid, activated=True).count()

    # Construir las consultas filtradas
    filter_params = Q()
    if formid:
        filter_params &= Q(SurveyForms_id=formid)

    # Filtrar los registros con status = 1 (completados)
    completed_query = (
        ValidationRegister.objects.filter(validationitems__rol_id__in=array_roles)
        .filter(filter_params & Q(status="si"))
        .values('document_number')
        .annotate(count=Count('id'))
    )

    # Filtrar los registros con status ≠ 1 (incompletos)
    uncompleted_query = (
        ValidationRegister.objects
        .filter(filter_params & Q(status="no"))  # Invertimos la condición
        .values('document_number')
        .annotate(count=Count('id'))
    )

    # Agregar al contexto
    context['validated_items'] = total_item
    context['validated_counts_completed'] = {entry['document_number']: entry['count'] for entry in completed_query}
    context['validated_counts_uncompleted'] = {entry['document_number']: entry['count'] for entry in uncompleted_query}
    return context

class CatatumboIndividualViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = CatatumboIndividualSerializer
    queryset = CatatumboIndividuales.objects.all()
    filter_backends = [ORFilterBackend]
    search_fields = ['identificacion',
        'nombre',
        'apellido'
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return setContext(context, self.kwargs.get('formid'))