from rest_framework import serializers
from ..models import FormCatatumboPreregistro

class CatatumboPreregistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCatatumboPreregistro
        fields = '__all__'