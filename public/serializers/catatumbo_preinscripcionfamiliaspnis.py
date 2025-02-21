from rest_framework import serializers
from ..models import FormCatatumboPreregistroFamiliasPnis

class CatatumboPreincripcionFamiliasPnisSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCatatumboPreregistroFamiliasPnis
        fields = '__all__'
        
        