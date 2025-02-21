from rest_framework import routers
from django.urls import path

#from .viewsets.customer import CustomerViewSet

router = routers.SimpleRouter()
#router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = router.urls + [

]