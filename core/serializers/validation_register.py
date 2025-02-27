from rest_framework import serializers
from core.models import ValidationArgeliaPersonas

class ValidationPersonasSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidationArgeliaPersonas
        fields = '__all__'