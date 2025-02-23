from rest_framework import serializers
from ..models import FormCatatumboPreinscripcionDesplazados

class CatatumboPreincripcionDesplazadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCatatumboPreinscripcionDesplazados
        fields = '__all__'