from rest_framework import routers
from django.urls import path

from .viewsets.archivo import ArchivoKeyViewSet, ArchivoViewSet
from .viewsets.staff import StaffViewSet,  UserPnisViewSet, ArgeliaGruposViewSet, ArgeliaPersonasViewSet, DepartmentViewSet, MunicipalityViewSet, TownshipViewSet, VillageViewSet, ValidationRegisterViewSet
from .apiview.user import UserAPIView

router = routers.SimpleRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'userpnis', UserPnisViewSet, basename='userpnis')
router.register(r'argeliagrupos', ArgeliaGruposViewSet, basename='argeliagrupos')
router.register(r'argeliapersonas', ArgeliaPersonasViewSet, basename='argeliapersonas')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'municipalities', MunicipalityViewSet, basename='municipalities')
router.register(r'townships', TownshipViewSet, basename='townships')
router.register(r'villages', VillageViewSet, basename='villages')
router.register(r'validationregister', ValidationRegisterViewSet, basename='validationregister')

urlpatterns = router.urls + [
    path('user/data/', UserAPIView.as_view(), name='get-user-data'),
    path('municipalities/by-department/<int:department_id>/', MunicipalityViewSet.as_view({'get': 'list'}), name='municipalities-by-department'),
    path('townships/by-municipality/<int:municipality_id>/', TownshipViewSet.as_view({'get': 'list'}), name='townships-by-municipality'),
    path('villages/by-township/<int:township_id>/', VillageViewSet.as_view({'get': 'list'}), name='villages-by-township'),
    
    path('media/generatekey/', ArchivoKeyViewSet.as_view({'get': 'generar'}), name='media-generar'),
    path('media/<str:key>/<int:uid>/', ArchivoViewSet.as_view({'get': 'descargar'}), name='media-descargar'),
    path('userpnis/filterbysurvey/<int:formid>/', UserPnisViewSet.as_view({'get': 'list'}), name='userpnis-filterbysurvey'),
    path('argeliagrupos/filterbysurvey/<int:formid>/', ArgeliaGruposViewSet.as_view({'get': 'list'}), name='argeliagrupos-filterbysurvey'),
    path('argeliapersonas/filterbysurvey/<int:formid>/', ArgeliaPersonasViewSet.as_view({'get': 'list'}), name='argeliapersonas-filterbysurvey'),
    path('validationregister/missing-validation-items/<str:document_number>/<int:survey_id>/', ValidationRegisterViewSet.as_view({'get': 'missing_validation_items'}), name='missing-validation-items'),
    path('validationregister/filterbydocumentnumber/<str:document_number>/<int:survey_id>/<str:status>/', ValidationRegisterViewSet.as_view({'get': 'filterbydocumentnumber'}), name='filterbydocumentnumber'),
    # path('user-pnis/data/<int:pnis_id>/', UserPnisAPIView.as_view(), name='user-pnis-detail'),  # Registro específico
]