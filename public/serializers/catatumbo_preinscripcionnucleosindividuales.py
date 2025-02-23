from rest_framework import serializers
from ..models import FormCatatumboPreinscripcionNucleosIndividuales
from pnis.mixins.baseImage import BaseImageMixin

class CatatumboPreincripcionNucleosIndividualesSerializer(BaseImageMixin, serializers.ModelSerializer):
    foto_frente = BaseImageMixin.url_image
    
    class Meta:
        model = FormCatatumboPreinscripcionNucleosIndividuales
        fields = '__all__'
        
        