from rest_framework import serializers
from ..models import FormCatatumboPreinscripcionGrupoProductores

class CatatumboPreincripcionGrupoProductoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCatatumboPreinscripcionGrupoProductores
        fields = '__all__'
        
        