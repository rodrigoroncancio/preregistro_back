from rest_framework import routers
from django.urls import path

from .viewsets.archivo import ArchivoKeyViewSet, ArchivoViewSet, ArchivoBase64ViewSet
from .viewsets.validation_register import ValidationFinalRegisterViewSet, ValidationRegisterViewSet, CedulasRnecViewSet
from .viewsets.staff import CatatumboFichaAcuerdoViewSet, CatatumboFichaAcuerdoNucleoViewSet, NucleoFamiliarViewSet, StaffViewSet, FichaAcuerdoFase2ViewSet, FichaAcuerdoFase2NucleoViewSet,  UserPnisViewSet, ArgeliaGruposViewSet, ArgeliaPersonasViewSet, DepartmentViewSet, MunicipalityViewSet, TownshipViewSet, VillageViewSet
from .viewsets.catatumbo import CatatumboIndividualViewSet, CatatumboGruposViewSet
from .viewsets.user import UserViewSet

router = routers.SimpleRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'userpnis', UserPnisViewSet, basename='userpnis')
router.register(r'argeliagrupos', ArgeliaGruposViewSet, basename='argeliagrupos')
router.register(r'argeliapersonas', ArgeliaPersonasViewSet, basename='argeliapersonas')
router.register(r'catatumboindividual', CatatumboIndividualViewSet, basename='catatumboindividual')
router.register(r'catatumbogrupos', CatatumboGruposViewSet, basename='catatumbogrupos')
router.register(r'fichaacuerdofase2', FichaAcuerdoFase2ViewSet, basename='fichaacuerdofase2')
router.register(r'catatumbofichaacuerdo', CatatumboFichaAcuerdoViewSet, basename='catatumbofichaacuerdo')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'municipalities', MunicipalityViewSet, basename='municipalities')
router.register(r'townships', TownshipViewSet, basename='townships')
router.register(r'villages', VillageViewSet, basename='villages')
router.register(r'validationregister', ValidationRegisterViewSet)
router.register(r'validationfinalregister', ValidationFinalRegisterViewSet)
router.register(r'cedulasrnec', CedulasRnecViewSet)

urlpatterns = router.urls + [
    path('validationregister/<int:pk>/delete/', ValidationRegisterViewSet.as_view({'delete': 'delete_by_id'}), name='validationregister-delete'),
    path('user/data/', UserViewSet.as_view({'get': 'user_data'}), name='get-user-data'),
    path('user/roles/', UserViewSet.as_view({'get': 'roles'}), name='get-user-roles'),
    path('municipalities/by-department/<int:department_id>/', MunicipalityViewSet.as_view({'get': 'list'}), name='municipalities-by-department'),
    path('townships/by-municipality/<int:municipality_id>/', TownshipViewSet.as_view({'get': 'list'}), name='townships-by-municipality'),
    path('villages/by-township/<int:township_id>/', VillageViewSet.as_view({'get': 'list'}), name='villages-by-township'),
    
    path('media/generatekey/', ArchivoKeyViewSet.as_view({'get': 'generar'}), name='media-generar'),
    path('media/<str:key>/<int:uid>/', ArchivoViewSet.as_view({'get': 'descargar'}), name='media-descargar'),
    path('mediabase64/<str:key>/<int:uid>/', ArchivoBase64ViewSet.as_view({'get': 'descargar'}), name='media-descargar'),
    path('userpnis/filterbysurvey/<int:formid>/', UserPnisViewSet.as_view({'get': 'list'}), name='userpnis-filterbysurvey'),
    path('userpnis/getnucleo/<str:documento>/', NucleoFamiliarViewSet.as_view({'get': 'list'}), name='userpnis-filterbysurvey'),
    path('argeliagrupos/filterbysurvey/<int:formid>/', ArgeliaGruposViewSet.as_view({'get': 'list'}), name='argeliagrupos-filterbysurvey'),
    path('argeliapersonas/filterbysurvey/<int:formid>/', ArgeliaPersonasViewSet.as_view({'get': 'list'}), name='argeliapersonas-filterbysurvey'),
    path('catatumboindividual/filterbysurvey/<int:formid>/<int:tipo>/', CatatumboIndividualViewSet.as_view({'get': 'list'}), name='argeliapersonas-filterbysurvey'),
    path('catatumbogrupos/filterbysurvey/<int:formid>/', CatatumboGruposViewSet.as_view({'get': 'list'}), name='argeliapersonas-filterbysurvey'),
    path('catatumbofichaacuerdo/filterbysurvey/<int:formid>/', CatatumboFichaAcuerdoViewSet.as_view({'get': 'list'}), name='catatumboficha-filterbysurvey'),
     path('fichaacuerdo2/getnucleo/<int:fichaid>/', FichaAcuerdoFase2NucleoViewSet.as_view({'get': 'list'}), name='ficha2-filterbysurvey'),
    path('catatumbofichaacuerdo/getnucleo/<int:fichaid>/', CatatumboFichaAcuerdoNucleoViewSet.as_view({'get': 'list'}), name='catatumboficha-filterbysurvey'),
    # path('validationregister/missing-validation-items/<str:document_number>/<int:survey_id>/', ValidationRegisterViewSet.as_view({'get': 'missing_validation_items'}), name='missing-validation-items'),
    # path('validationregister/filterbydocumentnumber/<str:document_number>/<int:survey_id>/<str:status>/', ValidationRegisterViewSet.as_view({'get': 'filterbydocumentnumber'}), name='filterbydocumentnumber'),
    # path('user-pnis/data/<int:pnis_id>/', UserPnisAPIView.as_view(), name='user-pnis-detail'),  # Registro específico
]