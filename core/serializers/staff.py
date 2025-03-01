from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
from pnis.mixins.baseImage import BaseImageMixin
from pnis.mixins.baseFile import BaseFileMixin
from core.models import Staff, UserPNIS, Department, Municipality, Township, Village, ArgeliaGrupos, ArgeliaPersonas, ValidationRegister
from public.models import FormArgeliaFichaAcuerdo

class UserPNISSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()

    class Meta:
        model = UserPNIS
        fields = '__all__'

    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.identificationnumber, 0)
        return f"{completed}/7"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.identificationnumber, 0)
        return f"{uncompleted}/7"

    
class ArgeliaGruposSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = ArgeliaGrupos
        fields = '__all__'
        
    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.cedularepresentante, 0)
        return f"{completed}/7"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.cedularepresentante, 0)
        return f"{uncompleted}/7"
    
class FichaAcuerdoFase2Serializer(serializers.ModelSerializer):    
    class Meta:
        model = FormArgeliaFichaAcuerdo
        fields = '__all__'
        
class ArgeliaPersonasSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = ArgeliaPersonas
        fields = '__all__'
        
    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.identificacion, 0)
        return f"{completed}/7"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.identificacion, 0)
        return f"{uncompleted}/7"


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

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'

class TownshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Township
        fields = '__all__'

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'

    
class StaffInfoSerializer(BaseImageMixin, serializers.ModelSerializer):
    url_image = BaseImageMixin.url_image

    class Meta:
        model = Staff
        fields = ['image', 'phone', 'url_image']

class StaffSerializer(BaseImageMixin, serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(source='staff.phone', read_only=True)
    staff_info = StaffInfoSerializer(source='staff')

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'password', 'phone', 'staff_info']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        staff_data = validated_data.pop('staff', None)

        validated_data['is_staff'] = True
        validated_data['username'] = validated_data['email']
        validated_data['last_login'] = timezone.now()
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()

        if staff_data:
            Staff.objects.create(user=user, **staff_data)

        return user

    def update(self, instance, validated_data):
        staff_data = validated_data.pop('staff', None)

        if not self.context['request'].user.is_superuser:
            validated_data.pop('is_superuser', None)

        password = validated_data.pop('password', None)
        validated_data.pop('email', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()

        if staff_data:
            staff_instance, created = Staff.objects.get_or_create(user=instance)
            for attr, value in staff_data.items():
                setattr(staff_instance, attr, value)
            staff_instance.save()

        return instance

class StaffListSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='staff.image', read_only=True)
    phone = serializers.CharField(source='staff.phone', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'is_active', 'is_superuser', 'image',]
