from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
from pnis.mixins.baseImage import BaseImageMixin
from core.models import PersonaPnis, NucleoFamiliarPersonas, Staff, RolUsuario, UserPNIS, ArgeliaGrupos, ArgeliaPersonas, VArgeliaIndividual
from public.models import FormArgeliaFichaAcuerdo, FormArgeliaFichaAcuerdoNucleoFamiliar, FormCatatumbosFichaAcuerdo

class NucleoFamiliarSerializer(serializers.ModelSerializer):

    class Meta:
        model = NucleoFamiliarPersonas
        fields = '__all__'
        
class PersonaPnisSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()

    class Meta:
        model = PersonaPnis
        fields = '__all__'        

class UserPNISSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()

    class Meta:
        model = UserPNIS
        fields = '__all__'

    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        count_items = self.context.get('validated_items', 0)
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.identificationnumber, 0)
        return f"{completed}/{count_items}"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.identificationnumber, 0)
        return f"{uncompleted}"

    
class ArgeliaGruposSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = ArgeliaGrupos
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
    
class FichaAcuerdoFase2Serializer(serializers.ModelSerializer):    
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = FormArgeliaFichaAcuerdo
        fields = '__all__'
        
    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        count_items = self.context.get('validated_items', 0)
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.numero_identificacion, 0)
        return f"{completed}/{count_items}"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.numero_identificacion, 0)
        return f"{uncompleted}"    
        
class FormFichaAcuerdoFase2NucleoFamiliarSerializer(serializers.ModelSerializer):    
    class Meta:
        model = FormArgeliaFichaAcuerdoNucleoFamiliar
        fields = '__all__'        
        
class CatatumboFichaAcuerdoSerializer(serializers.ModelSerializer):    
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = FormCatatumbosFichaAcuerdo
        fields = '__all__'   
        
    def get_number_completed(self, obj):
        # Obtiene el diccionario de conteo de registros completados
        count_items = self.context.get('validated_items', 0)
        completed_counts = self.context.get('validated_counts_completed', {})
        completed = completed_counts.get(obj.numero_identificacion, 0)
        return f"{completed}/{count_items}"

    def get_number_uncompleted(self, obj):
        # Obtiene el diccionario de conteo de registros incompletos
        uncompleted_counts = self.context.get('validated_counts_uncompleted', {})
        uncompleted = uncompleted_counts.get(obj.numero_identificacion, 0)
        return f"{uncompleted}"     
        
class ArgeliaPersonasSerializer(serializers.ModelSerializer):
    number_completed = serializers.SerializerMethodField()
    number_uncompleted = serializers.SerializerMethodField()
    class Meta:
        model = VArgeliaIndividual
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
    
class StaffInfoSerializer(BaseImageMixin, serializers.ModelSerializer):
    url_image = BaseImageMixin.url_image

    class Meta:
        model = Staff
        fields = ['image', 'phone', 'url_image']

class StaffSerializer(BaseImageMixin, serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(source='staff.phone', read_only=True)
    roles = serializers.SerializerMethodField()
    staff_info = StaffInfoSerializer(source='staff')

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email', 'is_active', 'roles', 'is_superuser', 'password', 'phone', 'staff_info']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_roles(self, obj):
        return list(obj.roles.values_list('rol_id', flat=True))

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
        roles = self.context['request'].data['roles'] or []

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

        if isinstance(roles, list) and roles:
            roles_actuales = instance.roles.all()    
            roles_a_eliminar = roles_actuales.exclude(rol_id__in=roles)
            roles_a_eliminar.delete()
            roles_a_agregar = [rol_id for rol_id in roles if not roles_actuales.filter(rol_id=rol_id).exists()]
            for rol_id in roles_a_agregar:
                RolUsuario.objects.create(user=instance, rol_id=rol_id)

        return instance

class StaffListSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='staff.image', read_only=True)
    phone = serializers.CharField(source='staff.phone', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'is_active', 'is_superuser', 'image',]

