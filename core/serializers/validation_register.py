from rest_framework import serializers
from pnis.mixins.baseFile import BaseFileMixin
from core.models import ValidationRegister, ValidationArgeliaPersonas, ValidationItems, CedulasRnec


class CedulasRnecSerializer(BaseFileMixin, serializers.ModelSerializer): 
    class Meta:
        model = CedulasRnec
        fields = '__all__'
            

class ValidationRegisterSerializer(BaseFileMixin, serializers.ModelSerializer): 
    attachment = BaseFileMixin.base64_file()
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = ValidationRegister
        fields = '__all__'
            
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)    
        
    def get_user_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name
    
class ValidationRegisterLiteSerializer(serializers.ModelSerializer): 
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = ValidationRegister
        fields = ['id', 'user_name', 'status', 'observation', 'attachment', 'validationitems_id']
        
    def get_user_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

class ValidationPersonasSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidationArgeliaPersonas
        fields = '__all__'

class ValidationItemsSerializer(serializers.ModelSerializer):
    rolname = serializers.CharField(source='rol.nombre')
    class Meta:
        model = ValidationItems
        fields = ['id', 'name', 'survey', 'rol', 'rolname']