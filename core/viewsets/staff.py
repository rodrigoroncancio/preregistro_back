from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAdminUser
from django.contrib.auth import get_user_model
from django.db.models import Count

from public.serializers.catatumbo_fichaacuerdo import FormCatatumboFichaAcuerdoNucleoFamiliarLeerSerializer, FormCatatumboFichaAcuerdoNucleoFamiliarSerializer
from public.models import FormArgeliaFichaAcuerdo, FormArgeliaFichaAcuerdoNucleoFamiliar, FormCatatumbosFichaAcuerdo, FormCatatumnoFichaAcuerdoNucleoFamiliar
from core.models import  NucleoFamiliarPersonas, UserPNIS, Department, Municipality, Township, Village, ArgeliaGrupos, ArgeliaPersonas, VArgeliaIndividual, ValidationRegister, ValidationItems
from core.serializers.staff import CatatumboFichaAcuerdoSerializer, NucleoFamiliarSerializer, StaffSerializer, StaffListSerializer, UserPNISSerializer, ArgeliaGruposSerializer, ArgeliaPersonasSerializer, FichaAcuerdoFase2Serializer, FormFichaAcuerdoFase2NucleoFamiliarSerializer
from core.serializers.list import DepartmentSerializer, MunicipalitySerializer, TownshipSerializer, VillageSerializer
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
        return setContext(context, self.kwargs.get('formid'))
        """
        auth = context['request'].auth
        array_roles = auth.payload["roles"]

        total_item = ValidationItems.objects.filter(rol_id__in=array_roles, survey=formid, activated=True).count()

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
        """

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
        return setContext(context, self.kwargs.get('formid'))

class FichaAcuerdoFase2ViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = FichaAcuerdoFase2Serializer
    queryset = FormArgeliaFichaAcuerdo.objects.all()
    filter_backends = [ORFilterBackend]
    search_fields = ['numero_identificacion',
        'nombre',
        'numero_identificacion'
    ]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        return setContext(context, self.kwargs.get('formid'))
    
class FichaAcuerdoFase2NucleoViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = FormFichaAcuerdoFase2NucleoFamiliarSerializer
    queryset = FormArgeliaFichaAcuerdoNucleoFamiliar.objects.all()
    filter_backends = [ORFilterBackend]
    
    def get_queryset(self):
        fichaid = self.kwargs.get('fichaid')  # Obtener el parámetro de la URL
        return FormArgeliaFichaAcuerdoNucleoFamiliar.objects.filter(ficha=fichaid) 
    
    
class CatatumboFichaAcuerdoViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = CatatumboFichaAcuerdoSerializer
    queryset = FormCatatumbosFichaAcuerdo.objects.all()
    filter_backends = [ORFilterBackend]
    search_fields = ['numero_identificacion',
        'nombre',
        'numero_identificacion'
    ]    
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        return setContext(context, self.kwargs.get('formid'))

class CatatumboFichaAcuerdoNucleoViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = FormCatatumboFichaAcuerdoNucleoFamiliarSerializer
    queryset = FormCatatumnoFichaAcuerdoNucleoFamiliar.objects.all()
    filter_backends = [ORFilterBackend]
    
    def get_queryset(self):
        fichaid = self.kwargs.get('fichaid')  # Obtener el parámetro de la URL
        return FormCatatumnoFichaAcuerdoNucleoFamiliar.objects.filter(ficha=fichaid) 
    
    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return FormCatatumboFichaAcuerdoNucleoFamiliarLeerSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)


class ArgeliaPersonasViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = ArgeliaPersonasSerializer
    queryset = VArgeliaIndividual.objects.all()
    filter_backends = [ORFilterBackend]
    search_fields = ['identificacion',
        'nombres',
        'apellidos'
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return setContext(context, self.kwargs.get('formid'))



class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def list(self, request):
        """ Devuelve la lista completa de departamentos """
        departments_list = Department.objects.all().values()
        return Response(list(departments_list))

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    
    
    

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
    
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

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
    
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

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
    
    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

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
            return get_user_model().objects.filter(id=user.id).all()
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
