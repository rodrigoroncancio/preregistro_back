from rest_framework import serializers
from ..models import FormArgeliaFichaAcuerdo, FormArgeliaFichaAcuerdoNucleoFamiliar
from pnis.mixins.baseFile import BaseFileMixin

class ArgeliaFichaAcuerdoSerializer(serializers.ModelSerializer):
    foto_doc_frente = BaseFileMixin.base64_file()
    foto_doc_atras = BaseFileMixin.base64_file()
    tipo_documento_file = BaseFileMixin.base64_file()
    predio1_documento_arraigo= BaseFileMixin.base64_file()
    predio2_documento_arraigo= BaseFileMixin.base64_file()
    predio3_documento_arraigo= BaseFileMixin.base64_file()
    predio4_documento_arraigo= BaseFileMixin.base64_file()
    predio5_documento_arraigo= BaseFileMixin.base64_file()
    predio6_documento_arraigo= BaseFileMixin.base64_file()
    predio7_documento_arraigo= BaseFileMixin.base64_file()
    predio8_documento_arraigo= BaseFileMixin.base64_file()
    predio9_documento_arraigo= BaseFileMixin.base64_file()
    predio10_documento_arraigo= BaseFileMixin.base64_file()
    
    predio1_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio2_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio3_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio4_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio5_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio6_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio7_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio8_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio9_arraigo_documento_soporte= BaseFileMixin.base64_file()
    predio10_arraigo_documento_soporte= BaseFileMixin.base64_file()
    firma_file= BaseFileMixin.base64_file()
    
    documento_pertenencia_etnica_file= BaseFileMixin.base64_file()

    class Meta:
        model = FormArgeliaFichaAcuerdo
        fields = '__all__'
        
class FormArgeliaFichaAcuerdoNucleoFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormArgeliaFichaAcuerdoNucleoFamiliar
        fields = '__all__'  # Serializa todos los campos


        
        