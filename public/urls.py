from rest_framework import routers
from django.urls import path

from .views.catatumbo import *

router = routers.SimpleRouter()
#router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('forms/catatumbo/validar_documento/', CatatumboValidaDocumentoView.as_view(), name='catatumbo-valida-documento'),
    path('forms/catatumbo/preregistro/', CatatumboPreregistroView.as_view(), name='catatumbo-preregistro'),
    path('forms/catatumbo/preinscripcionnucleo/', CatatumboPreinscripcionNucleoView.as_view(), name='catatumbo-preinscripcionnucleo'),
    path('forms/catatumbo/preinscripciondesplazados/', CatatumboPreinscripcionDesplazdosView.as_view(), name='catatumbo-preinscripciondesplazados'),
    path('forms/catatumbo/preinscripciongrupoproductores/', CatatumboPreinscripcionGrupoProductoresView.as_view(), name='catatumbo-preinscripciondesgruposproductores'),
    path('forms/catatumbo/preinscripcionnucleosindividuales/', CatatumboPreinscripcionNucleosIndividualesView.as_view(), name='catatumbo-preinscripciondesNucleosIndividuales'),
    path('forms/catatumbo/preinscripcionfamiliaspnis/', CatatumboPreinscripcionFamiliasPnisView.as_view(), name='catatumbo-preinscripciondesFamiliasPnis'),
]