# from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from pnis.mixins.baseImage import BaseImageMixin
from core.models import CatatumboIndividuales, CatatumboGrupo
# from public.models import FormArgeliaFichaAcuerdo

class CatatumboIndividualSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = CatatumboIndividuales
        fields = '__all__'
        
    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        count_items = self.context.get('validated_items', 0)
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.identificacion, 0)
        return f"{completed}/{count_items}"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.identificacion, 0)
        return f"{uncompleted}"
    
    
class CatatumboGrupoSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = CatatumboGrupo
        fields = '__all__'
        
    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        count_items = self.context.get('validated_items', 0)
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.cedula_representante, 0)
        return f"{completed}/{count_items}"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.cedula_representante, 0)
        return f"{uncompleted}"    