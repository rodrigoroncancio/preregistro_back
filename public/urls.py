from rest_framework import routers
from django.urls import path

from .views.catatumbo import *

router = routers.SimpleRouter()
#router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('public/consultar_documento/<int:doc>/<str:fecha>', ConsultarDocumentoView.as_view({'get':'consultar'}), name='consultar-documento'),
    path('catatumbo/validar_documento/', CatatumboValidaDocumentoView.as_view(), name='catatumbo-valida-documento'),
    path('catatumbo/ficha/validar_documento/', CatatumboFichaValidaDocumentoView.as_view(), name='catatumbo-ficha-valida-documento'),
    path('catatumbo/ficha/validar_nucleo/', CatatumboFichaValidaNucleoView.as_view(), name='catatumbo-ficha-valida-nucleo'),
    path('argelia/ficha/validar_documento/', ArgeliaFichaValidaDocumentoView.as_view(), name='argelia-ficha-valida-documento'),
    path('catatumbo/preregistro/', CatatumboPreregistroView.as_view(), name='catatumbo-preregistro'),
    path('catatumbo/preinscripcionnucleo/', CatatumboPreinscripcionNucleoView.as_view(), name='catatumbo-preinscripcionnucleo'),
    path('catatumbo/preinscripciondesplazados/', CatatumboPreinscripcionDesplazdosView.as_view(), name='catatumbo-preinscripciondesplazados'),
    path('catatumbo/preinscripciongrupoproductores/', CatatumboPreinscripcionGrupoProductoresView.as_view(), name='catatumbo-preinscripciondesgruposproductores'),
    path('catatumbo/preinscripcionnucleosindividuales/', CatatumboPreinscripcionNucleosIndividualesView.as_view(), name='catatumbo-preinscripciondesNucleosIndividuales'),
    path('catatumbo/preinscripcionfamiliaspnis/', CatatumboPreinscripcionFamiliasPnisView.as_view(), name='catatumbo-preinscripciondesFamiliasPnis'),
    path('argelia/fichaacuerdo/', ArgeliaFichaAcuerdoView.as_view(), name='argelia-fichaacuerdo'),
    path('argelia/fichaacuerdonucleo/', ArgeliaFichaAcuerdoNucleoView.as_view(), name='argelia-fichaacuerdo'),
    path('catatumbo/fichaacuerdo/', CatatumboFichaAcuerdoView.as_view(), name='argelia-fichaacuerdo'),
    path('catatumbo/fichaacuerdonucleo/', CatatumboFichaAcuerdoNucleoView.as_view(), name='argelia-fichaacuerdo'),
    
]