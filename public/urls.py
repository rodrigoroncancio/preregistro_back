from rest_framework import routers
from django.urls import path

from .views.catatumbo import *

router = routers.SimpleRouter()
#router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('forms/catatumbo/validar_documento/', CatatumboValidaDocumentoView.as_view(), name='catatumbo-valida-documento'),
    path('forms/catatumbo/preregistro/', CatatumboPreregistroView.as_view(), name='catatumbo-preregistro'),
]