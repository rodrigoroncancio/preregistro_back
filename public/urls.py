from rest_framework import routers
from django.urls import path

from .views.catatumbo import CatatumboPreregistroView

router = routers.SimpleRouter()
#router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('forms/catatumbo/preregistro/', CatatumboPreregistroView.as_view(), name='catatumbo-preregistro'),
]