from rest_framework import serializers
from ..models import FormCatatumboPreinscripcionNucleo

class CatatumboPreincripcionNucleoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCatatumboPreinscripcionNucleo
        fields = '__all__'