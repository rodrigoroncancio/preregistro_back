from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAdminUser
from django.contrib.auth import get_user_model
from django.db.models import Count

from public.models import FormArgeliaFichaAcuerdo
from core.models import NucleoFamiliarPersonas, UserPNIS, Department, Municipality, Township, Village, ArgeliaGrupos, ArgeliaPersonas, ValidationRegister, ValidationItems
from core.serializers.staff import NucleoFamiliarSerializer, StaffSerializer, StaffListSerializer, UserPNISSerializer, DepartmentSerializer, MunicipalitySerializer, TownshipSerializer, VillageSerializer, ArgeliaGruposSerializer, ArgeliaPersonasSerializer, FichaAcuerdoFase2Serializer
from pnis.filters import ORFilterBackend

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    
class NucleoFamiliarViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = NucleoFamiliarSerializer
    queryset = NucleoFamiliarPersonas.objects.all()
   
    def get_queryset(self):
        documento = self.kwargs.get('documento')  # Obtener el parámetro de la URL
        return NucleoFamiliarPersonas.objects.filter(titular_identificacion=documento)  # Filtrar por titular_identificacion

class UserPnisViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserPNISSerializer
    queryset = UserPNIS.objects.filter(signature__isnull=False).all()
    filter_backends = [ORFilterBackend]
    search_fields = ['identificationnumber',
        'name',
        'lastname'
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()

        # Obtener el parámetro desde la URL
        formid = self.kwargs.get('formid')

        # Construir las consultas filtradas
        filter_params = Q()
        if formid:
            filter_params &= Q(SurveyForms_id=formid)

        # Filtrar los registros con status = 1 (completados)
        completed_query = (
            ValidationRegister.objects
            .filter(filter_params & Q(status="si"))
            .values('document_number')
            .annotate(count=Count('id'))
        )

        # Filtrar los registros con status ≠ 1 (incompletos)
        uncompleted_query = (
            ValidationRegister.objects
            .filter(filter_params & ~Q(status="si"))  # Invertimos la condición
            .values('document_number')
            .annotate(count=Count('id'))
        )

        # Convertir a diccionarios para acceso rápido
        completed_dict = {entry['document_number']: entry['count'] for entry in completed_query}
        uncompleted_dict = {entry['document_number']: entry['count'] for entry in uncompleted_query}

        # Agregar al contexto
        context['validated_counts_completed'] = completed_dict
        context['validated_counts_uncompleted'] = uncompleted_dict
        return context

class ArgeliaGruposViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = ArgeliaGruposSerializer
    queryset = ArgeliaGrupos.objects.all()
    filter_backends = [ORFilterBackend]
    search_fields = ['identificacionorganizacion',
        'cedularepresentante',
        'grupoproductores',
        'departamentoinfluencia',
        'municipioinfluencia'
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()

        # Obtener el parámetro desde la URL
        formid = self.kwargs.get('formid')
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

        # Convertir a diccionarios para acceso rápido
        completed_dict = {entry['document_number']: entry['count'] for entry in completed_query}
        uncompleted_dict = {entry['document_number']: entry['count'] for entry in uncompleted_query}

        # Agregar al contexto
        context['validated_items'] = total_item
        context['validated_counts_completed'] = completed_dict
        context['validated_counts_uncompleted'] = uncompleted_dict
        return context

class FichaAcuerdoFase2ViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = FichaAcuerdoFase2Serializer
    queryset = FormArgeliaFichaAcuerdo.objects.all()
    filter_backends = [ORFilterBackend]
    search_fields = ['numero_identificacion',
        'nombre',
        'numero_identificacion'
    ]


class ArgeliaPersonasViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = ArgeliaPersonasSerializer
    queryset = ArgeliaPersonas.objects.all()
    filter_backends = [ORFilterBackend]
    search_fields = ['identificacion',
        'nombres',
        'apellidos'
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()

        # Obtener el parámetro desde la URL
        formid = self.kwargs.get('formid')
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

        # Convertir a diccionarios para acceso rápido
        completed_dict = {entry['document_number']: entry['count'] for entry in completed_query}
        uncompleted_dict = {entry['document_number']: entry['count'] for entry in uncompleted_query}

        # Agregar al contexto
        context['validated_items'] = total_item
        context['validated_counts_completed'] = completed_dict
        context['validated_counts_uncompleted'] = uncompleted_dict
        return context

class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def list(self, request):
        """ Devuelve la lista completa de departamentos """
        departments_list = Department.objects.all().values()
        return Response(list(departments_list))

class MunicipalityViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()

    def list(self, request, *args, **kwargs):
        """ Devuelve la lista de municipios, filtrada por departamento si se especifica department_id """
        department_id = kwargs.get('department_id')  # ← Capturar desde kwargs

        if department_id:
            municipalities_list = Municipality.objects.filter(departmentid=department_id).values()
        else:
            municipalities_list = Municipality.objects.all().values()

        return Response(list(municipalities_list))

class TownshipViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = TownshipSerializer
    queryset = Township.objects.all()

    def list(self, request, *args, **kwargs):
        """ Devuelve la lista de corregimientos filtrados por municipio si se proporciona municipality_id """
        municipality_id = kwargs.get('municipality_id')  # Capturar el ID desde la URL

        if municipality_id:
            townships_list = Township.objects.filter(municipalityid=municipality_id).values()
        else:
            townships_list = Township.objects.all().values()

        return Response(list(townships_list))

class VillageViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = VillageSerializer
    queryset = Village.objects.all()

    def list(self, request, township_id=None):
        """ Devuelve la lista de veredas filtradas por township_id """
        if township_id is not None:
            villages_list = Village.objects.filter(townshipid=township_id).values()
        else:
            villages_list = Village.objects.all().values()

        return Response(list(villages_list))

class StaffViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = StaffSerializer
    filter_backends = [ORFilterBackend]
    search_fields = ['first_name', 'last_name']


    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return get_user_model().objects.filter(Q(is_superuser=True) | Q(is_staff=True)).all()
        elif user.is_staff:
            return get_user_model().objects.filter(Q(is_superuser=True) | Q(is_staff=True)).filter(id=user.id).all()
        return get_user_model().objects.none()

    @action(detail=False, methods=['get'], url_path='lts')
    def lts(self, request):
        queryset = self.get_queryset().select_related('staff').all()
        serializer = StaffListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='password')
    def password(self, request, *args, **kwargs):
        password = request.data.get('password')
        user = get_user_model().objects.filter(id=kwargs['pk']).first()
        user.set_password(password)
        user.save()
        return Response({})
