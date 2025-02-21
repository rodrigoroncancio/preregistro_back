import json
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAdminUser
from django.contrib.auth import get_user_model

from core.models import Staff, UserPNIS, Department, Municipality, Township, Village
from core.serializers.staff import StaffSerializer, StaffListSerializer, UserPNISSerializer, DepartmentSerializer, MunicipalitySerializer, TownshipSerializer, VillageSerializer

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    
class UserPnisViewSet (viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    serializer_class = UserPNISSerializer
    queryset = UserPNIS.objects.all()

    def list(self, request):
        """ Devuelve la lista completa de usuarios PNIS """
        user_pnis_list = UserPNIS.objects.all().values()
        return Response(list(user_pnis_list))

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
