from rest_framework import routers
from django.urls import path

from .viewsets.staff import StaffViewSet,  UserPnisViewSet, DepartmentViewSet, MunicipalityViewSet, TownshipViewSet, VillageViewSet
from .apiview.user import UserAPIView

router = routers.SimpleRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'userpnis', UserPnisViewSet, basename='userpnis')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'municipalities', MunicipalityViewSet, basename='municipalities') 
router.register(r'townships', TownshipViewSet, basename='townships')
router.register(r'villages', VillageViewSet, basename='villages')



urlpatterns = router.urls + [
    path('user/data/', UserAPIView.as_view(), name='get-user-data'),
    path('municipalities/by-department/<int:department_id>/', MunicipalityViewSet.as_view({'get': 'list'}), name='municipalities-by-department'),
    path('townships/by-municipality/<int:municipality_id>/', TownshipViewSet.as_view({'get': 'list'}), name='townships-by-municipality'),
    path('villages/by-township/<int:township_id>/', VillageViewSet.as_view({'get': 'list'}), name='villages-by-township'),
    
    # path('user-pnis/data/<int:pnis_id>/', UserPnisAPIView.as_view(), name='user-pnis-detail'),  # Registro específico
]