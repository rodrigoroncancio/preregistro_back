import json
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAdminUser
from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import status

from core.models import Staff, UserPNIS, Department, Municipality, Township, Village, ArgeliaGrupos, ArgeliaPersonas, ValidationRegister, ValidationItems
from core.serializers.staff import StaffSerializer, StaffListSerializer, UserPNISSerializer, DepartmentSerializer, MunicipalitySerializer, TownshipSerializer, VillageSerializer, ArgeliaGruposSerializer, ArgeliaPersonasSerializer,ValidationRegisterSerializer

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    
class UserPnisViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserPNISSerializer
    queryset = UserPNIS.objects.all()

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
    
class ArgeliaPersonasViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = ArgeliaPersonasSerializer
    queryset = ArgeliaPersonas.objects.all()   
    
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
    
class ValidationRegisterViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = ValidationRegisterSerializer
    queryset = ValidationRegister.objects.all()   
    
    @action(detail=False, methods=['get'], url_path='missing-validation-items/<str:document_number>/<int:survey_id>/')
    def missing_validation_items(self, request, document_number, survey_id):
        # Obtener los ValidationItems registrados en ValidationRegister con ese document_number y survey_id
        registered_items = ValidationRegister.objects.filter(
            document_number=document_number, 
            SurveyForms_id=survey_id
        ).values_list('validationitems_id', flat=True)

        # Obtener los ValidationItems que no están registrados
        missing_items = ValidationItems.objects.exclude(id__in=registered_items)

        # Serializar los resultados
        return Response({"missing_items": list(missing_items.values())})
    

class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def list(self, request):
        """ Devuelve la lista completa de departamentos """
        departments_list = Department.objects.all().values()
        return Response(list(departments_list))

class MunicipalityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser] 
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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]
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
