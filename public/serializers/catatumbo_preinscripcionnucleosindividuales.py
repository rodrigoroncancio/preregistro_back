from rest_framework import serializers
from ..models import FormCatatumboPreinscripcionNucleosIndividuales

class CatatumboPreincripcionNucleosIndividualesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCatatumboPreinscripcionNucleosIndividuales
        fields = '__all__'
        
        