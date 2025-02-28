from django.db import models

# Create your models here.
class FormCatatumboPreregistro(models.Model):
    posee_predios = models.BooleanField(blank=True, null=True)
    numero_documento = models.CharField(max_length=50, blank=True, null=True)
    victima_desplazamiento = models.BooleanField(blank=True, null=True)
    actividades_transitar = models.CharField(max_length=255, blank=True, null=True)
    actividades_economicas = models.CharField(max_length=255, blank=True, null=True)
    linea_productiva = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.numero_documento if self.numero_documento else "Preinscripción"


class FormCatatumboPreinscripcionNucleo(models.Model):
    ocupa_predio_cultivo_ilicito = models.BooleanField(blank=True, null=True)
    numero_documento = models.CharField(max_length=20, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Preinscripción {self.numero_documento}"
    
class FormCatatumboPreinscripcionDesplazados(models.Model):
    ocupa_predio_cultivo_ilicito = models.BooleanField()
    numero_documento = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.codigo if self.codigo else 'Sin código'}"
    
    
class FormCatatumboPreinscripcionGrupoProductores(models.Model):
    ocupacion_asociados = models.BooleanField()
    victimas_desplazamiento = models.BooleanField(blank=True, null=True)
    actividad_transito = models.CharField(max_length=50, blank=True, null=True)
    actividad_etapa = models.CharField(max_length=50, blank=True, null=True)
    linea_productiva = models.CharField(max_length=50, blank=True, null=True)
    linea_productiva_otra = models.CharField(max_length=100, blank=True, null=True)
    actividad_economica = models.CharField(max_length=100, blank=True, null=True)
    experiencia_tiene_experiencia = models.BooleanField(blank=True, null=True)
    experiencia_agnos = models.FloatField(blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    municipio = models.CharField(max_length=50, blank=True, null=True)
    vereda = models.CharField(max_length=100, blank=True, null=True)
    grupo_nombre = models.CharField(max_length=200)
    grupo_tipo = models.CharField(max_length=100)
    grupo_num_registro = models.CharField(max_length=100, blank=True, null=True)
    lider_nombre = models.CharField(max_length=200)
    lider_identificacion = models.CharField(max_length=50)
    grupo_telefonos = models.CharField(max_length=200, blank=True, null=True)
    grupo_email = models.EmailField(max_length=100, blank=True, null=True)
    departamento_cobertura = models.CharField(max_length=100)
    veredas_cobertura = models.CharField(max_length=200)
    grupo_fecha_creacion = models.DateField()
    lineas_productivas = models.TextField()
    lineas_otro = models.CharField(max_length=200, blank=True, null=True)
    departamento_creacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.grupo_nombre} - {self.actividad_transito}"

class FormCatatumboPreinscripcionNucleosIndividuales(models.Model):

    ocupacion_beneficiario = models.BooleanField()
    numero_documento = models.CharField(max_length=20, blank=True, null=True)
    victimas_desplazamiento = models.BooleanField()
    actividad_transito = models.CharField(max_length=50, blank=True, null=True)
    actividad_etapa = models.CharField(max_length=50)
    actividad_economica = models.CharField(max_length=100, blank=True, null=True)
    experiencia_tiene_experiencia = models.BooleanField()
    experiencia_agnos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tiene_formacion = models.BooleanField()
    
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    cabecera_centropoblado = models.CharField(max_length=255)
    direccion = models.TextField()
    
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=100)  # Cédula, PEP, etc.
    numero_documento = models.CharField(max_length=50, unique=True)
    foto_frente = models.TextField(null=True, blank=True)
    foto_respaldo = models.TextField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=50, null=True, blank=True)  # Masculino, Femenino, etc.
    tiene_identidad_genero = models.BooleanField(null=True, blank=True)
    numero_celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # Identificación étnica
    etnia_identificacion = models.CharField(max_length=100, null=True, blank=True)  # Indígena, Afrocolombiano, etc.
    organizacion_pertenece = models.CharField(max_length=255, null=True, blank=True)  # Comunidad indígena, JAC, etc.
    resguardo_nombre = models.CharField(max_length=255, null=True, blank=True)
    ubicado_territorio_etnico = models.CharField(max_length=100, null=True, blank=True)  # Sí, No, No Sabe

    # Condiciones especiales
    condicion = models.CharField(max_length=100, null=True, blank=True)  # Víctima, Desplazado, Ninguno
    discapacidad = models.BooleanField(null=True, blank=True)
    educacion = models.CharField(max_length=100, null=True, blank=True)  # Primaria, Bachillerato, Técnico, etc.

    # Datos del núcleo familiar
    num_personas_nucleo = models.PositiveIntegerField(null=True, blank=True)
    num_doc_personas_nucleo = models.TextField(null=True, blank=True)  # Documentos separados por guion
    nombres_apellidos_nucleo = models.TextField(null=True, blank=True)  # Nombres completos separados por guion

    # Información general del predio
    num_predios_relevancia = models.CharField(max_length=50, null=True, blank=True)  # 2 Predio, 3 Predio, etc.
    municipio = models.CharField(max_length=100, null=True, blank=True)
    vereda = models.CharField(max_length=255, null=True, blank=True)
    vereda_otro = models.CharField(max_length=255, null=True, blank=True)  # Si es otro
    descripcion_acceso = models.TextField(null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    
    # Área del predio
    area_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    area_coca = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Relación de tenencia
    relacion_tenencia = models.CharField(max_length=100, null=True, blank=True)  # Propietario, Poseedor, Ocupante

    # Documentos (cada uno en su propio campo)
    foto_relacion_tenencia = models.TextField( null=True, blank=True)
    
    # Ubicación geográfica
    longitud = models.CharField(max_length=50, null=True, blank=True)
    latitud = models.CharField(max_length=50, null=True, blank=True)
    altitud = models.CharField(max_length=50, null=True, blank=True)
    precision = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return f"Preinscripción de {self.numero_documento or 'Sin Documento'}"
    
from django.db import models

class FormCatatumboPreregistroFamiliasPnis(models.Model):
    # Página 1: Validación de datos
    numero_documento = models.CharField(max_length=20, unique=True, verbose_name="Número de documento")
    victima_desplazamiento = models.BooleanField(null=True, blank=True, verbose_name="¿Ha sido víctima de desplazamiento forzado después del 15 de enero de 2025?")

    # Página 2: Datos personales
    nombres = models.CharField(max_length=255, verbose_name="Nombres")
    apellidos = models.CharField(max_length=255, verbose_name="Apellidos")
    numero_telefono = models.CharField(max_length=100, null=True, blank=True, verbose_name="Número de teléfono celular")
    email = models.EmailField(verbose_name="Correo electrónico")

    # Página 3: Ubicación y aceptación de términos
    departamento = models.CharField(max_length=100, verbose_name="Departamento")
    municipio = models.CharField(max_length=100, null=True, blank=True, verbose_name="Municipio")
    vereda = models.CharField(max_length=100, null=True, blank=True, verbose_name="Veredafamilias")
    direccion = models.TextField(null=True, blank=True, verbose_name="Dirección o referencia del predio")
    
    # Aceptación de términos
    acepta_terminos = models.CharField(max_length=2,null=True, blank=True, verbose_name="Acepta términos y condiciones")
    acepta_tratamiento_datos = models.CharField(max_length=2,null=True, blank=True,verbose_name="Acepta tratamiento de datos personales")

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.numero_documento}"


class FormArgeliaFichaAcuerdo(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    tipo_identificacion = models.CharField(max_length=50, blank=True, null=True)
    tipo_identificacion_cual = models.CharField(max_length=255, blank=True, null=True)
    numero_identificacion = models.CharField(max_length=50, unique=True, blank=True, null=True)
    foto_doc_frente = models.TextField( blank=True, null=True)
    foto_doc_atras = models.TextField( blank=True, null=True)
    fecha_expedicion = models.DateField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_contacto = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    identidad_genero = models.CharField(max_length=10, blank=True, null=True)
    estado_civil = models.CharField(max_length=50, blank=True, null=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    escolaridad = models.CharField(max_length=50, blank=True, null=True)
    escolaridad_otro = models.CharField(max_length=255, blank=True, null=True)
    tipo_salud = models.CharField(max_length=50, blank=True, null=True)
 

    grupo_especial = models.TextField(default=list, blank=True)
    comunidad_etnica = models.CharField(max_length=100, blank=True, null=True)
    pueblo_indigena = models.CharField(max_length=255, blank=True, null=True)
    organizacion_etnica = models.CharField(max_length=255, blank=True, null=True)
    nombre_territorio_etnico = models.CharField(max_length=255, blank=True, null=True)
    nombre_comunidad_etnica = models.CharField(max_length=255, blank=True, null=True)
    debidamente_inscrito = models.CharField(max_length=10, blank=True, null=True)

    ubicado_territorio_etnico = models.CharField(max_length=10,  blank=True, null=True)
    valor_ingresos = models.IntegerField(blank=True, null=True)
    valor_gastos = models.IntegerField(blank=True, null=True)
    
    departamento = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    vereda = models.CharField(max_length=255, blank=True, null=True)
    predio_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio_area = models.FloatField(blank=True, null=True)
    
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    altura = models.CharField(max_length=50, blank=True, null=True)
    permanencia = models.CharField(max_length=50, blank=True, null=True)
    tipo_relacion = models.CharField(max_length=255, blank=True, null=True)
    
    tipo_documento_acredita = models.CharField(max_length=255, blank=True, null=True)
    tipo_documento_file = models.TextField(blank=True, null=True)
    propietario_tipo_identificacion = models.CharField(max_length=50,  blank=True, null=True)
    propietario_numero_identificacion = models.CharField(max_length=50, blank=True, null=True)
    predio_mismo_residencia = models.CharField(max_length=10, blank=True, null=True)
    num_dependientes = models.IntegerField(blank=True, null=True)
    caracterizacion_productiva = models.TextField(blank=True, null=True)
    
    numero_predios_uso_ilicito = models.CharField(max_length=255, blank=True, null=True)
    
    predio1_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio1_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio1_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio1_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio1_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio1_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio1_num_plantas = models.IntegerField( blank=True, null=True)
    predio1_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio1_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio1_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio1_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio1_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio1_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio1_documento_arraigo = models.TextField( blank=True, null=True)
    predio1_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio1_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio1_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio1_arraigo_documento_soporte = models.TextField( blank=True, null=True)
    predio1_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio1_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio1_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio1_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio1_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio1_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio1_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio1_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio1_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    predio2_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio2_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio2_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio2_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio2_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio2_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio2_num_plantas = models.IntegerField( blank=True, null=True)
    predio2_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio2_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio2_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio2_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio2_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio2_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio2_documento_arraigo = models.FileField(blank=True, null=True)
    predio2_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio2_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio2_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio2_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio2_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio2_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio2_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio2_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio2_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio2_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio2_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio2_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio2_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    predio3_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio3_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio3_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio3_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio3_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio3_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio3_num_plantas = models.IntegerField( blank=True, null=True)
    predio3_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio3_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio3_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio3_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio3_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio3_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio3_documento_arraigo = models.FileField(blank=True, null=True)
    predio3_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio3_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio3_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio3_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio3_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio3_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio3_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio3_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio3_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio3_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio3_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio3_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio3_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    
    predio4_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio4_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio4_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio4_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio4_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio4_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio4_num_plantas = models.IntegerField( blank=True, null=True)
    predio4_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio4_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio4_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio4_altura = models.CharField(max_length=50, help_text="msnm", blank=True, null=True)
    predio4_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio4_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio4_documento_arraigo = models.FileField(blank=True, null=True)
    predio4_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio4_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio4_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio4_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio4_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio4_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio4_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio4_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio4_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio4_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio4_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio4_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio4_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    predio5_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio5_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio5_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio5_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio5_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio5_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio5_num_plantas = models.IntegerField( blank=True, null=True)
    predio5_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio5_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio5_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio5_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio5_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio5_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio5_documento_arraigo = models.FileField(blank=True, null=True)
    predio5_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio5_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio5_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio5_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio5_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio5_numero_nucleo_familiar = models.IntegerField(blank=True, null=True)
    predio5_numero_nucleo_no_familair = models.IntegerField(blank=True, null=True)
    predio5_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio5_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio5_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio5_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio5_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio5_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    
    predio6_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio6_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio6_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio6_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio6_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio6_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio6_num_plantas = models.IntegerField( blank=True, null=True)
    predio6_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio6_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio6_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio6_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio6_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio6_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio6_documento_arraigo = models.TextField( blank=True, null=True)
    predio6_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio6_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio6_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio6_arraigo_documento_soporte = models.TextField( blank=True, null=True)
    predio6_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio6_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio6_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio6_area_productiva = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True, null=True)
    predio6_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio6_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio6_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio6_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio6_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    predio7_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio7_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio7_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio7_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio7_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio7_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio7_num_plantas = models.IntegerField( blank=True, null=True)
    predio7_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio7_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio7_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio7_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio7_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio7_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio7_documento_arraigo = models.FileField(blank=True, null=True)
    predio7_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio7_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio7_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio7_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio7_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio7_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio7_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio7_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio7_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio7_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio7_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio7_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio7_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    predio8_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio8_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio8_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio8_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio8_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio8_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio8_num_plantas = models.IntegerField( blank=True, null=True)
    predio8_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio8_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio8_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio8_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio8_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio8_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio8_documento_arraigo = models.FileField(blank=True, null=True)
    predio8_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio8_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio8_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio8_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio8_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio8_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio8_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio8_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio8_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio8_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio8_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio8_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio8_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    
    predio9_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio9_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio9_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio9_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio9_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio9_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio9_num_plantas = models.IntegerField( blank=True, null=True)
    predio9_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio9_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio9_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio9_altura = models.CharField(max_length=50, help_text="msnm", blank=True, null=True)
    predio9_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio9_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio9_documento_arraigo = models.FileField(blank=True, null=True)
    predio9_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio9_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio9_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio9_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio9_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio9_numero_nucleo_familiar = models.IntegerField( blank=True, null=True)
    predio9_numero_nucleo_no_familair = models.IntegerField( blank=True, null=True)
    predio9_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio9_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio9_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio9_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio9_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio9_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    predio10_departamento = models.CharField(max_length=255, blank=True, null=True)
    predio10_municipio = models.CharField(max_length=255, blank=True, null=True)
    predio10_vereda = models.CharField(max_length=255, blank=True, null=True)
    predio10_nombre = models.CharField(max_length=255, blank=True, null=True)
    predio10_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio10_area_coca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio10_num_plantas = models.IntegerField( blank=True, null=True)
    predio10_area_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio10_longitud = models.CharField(max_length=50, blank=True, null=True)
    predio10_latitud = models.CharField(max_length=50, blank=True, null=True)
    predio10_altura = models.CharField(max_length=50, blank=True, null=True, help_text="msnm")
    predio10_arraigo_tiempo = models.IntegerField(help_text="Tiempo en años de permanencia en el municipio", blank=True, null=True)
    predio10_arraigo_anexa_documento = models.CharField(max_length=2, blank=True, null=True)
    predio10_documento_arraigo = models.FileField(blank=True, null=True)
    predio10_relacion_predio = models.CharField(max_length=255, blank=True, null=True)
    predio10_relacion_documento_acreditado = models.CharField(max_length=255, blank=True, null=True)
    predio10_arraigo_documento_anexo = models.CharField(max_length=2, blank=True, null=True)
    predio10_arraigo_documento_soporte = models.FileField(blank=True, null=True)
    predio10_todos_familiares = models.CharField(max_length=2, blank=True, null=True)
    predio10_numero_nucleo_familiar = models.IntegerField(blank=True, null=True)
    predio10_numero_nucleo_no_familair = models.IntegerField(blank=True, null=True)
    predio10_area_productiva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predio10_actividades_licitas_tiene = models.CharField(max_length=10, blank=True, null=True)
    predio10_actividades_licitas_lista = models.CharField(max_length=500, blank=True, null=True)
    predio10_actividades_licitas_lista_otra = models.CharField(max_length=10, blank=True, null=True)
    predio10_nucleo_unico_usufructa= models.CharField(max_length=10, blank=True, null=True)
    predio10_num_familias_usufructa= models.IntegerField(blank=True, null=True)
    
    nucleo_usufructa_otro = models.CharField(max_length=10, blank=True, null=True)
    actividades_otro_predio = models.TextField(blank=True, null=True)  # Se almacena como texto separado por comas
    actividad_otro_predio_otra = models.CharField(max_length=255, blank=True, null=True)

    linea_productiva = models.CharField(max_length=255, blank=True, null=True)
    establecimiento = models.CharField(max_length=10, blank=True, null=True)
    fortalecimiento = models.CharField(max_length=10, blank=True, null=True)
    tipo_figura_organizativa = models.CharField(max_length=255, blank=True, null=True)
    tipo_figura_organizativa_identificacion = models.CharField(max_length=255, blank=True, null=True)
    documento_pertenencia_etnica_anexa = models.CharField(max_length=10, blank=True, null=True)
    documento_pertenencia_etnica_file = models.TextField( blank=True, null=True)



    def __str__(self):
        return f"{self.nombre} - {self.numero_identificacion}"
    
    
class FormArgeliaFichaAcuerdoNucleoFamiliar (models.Model):
    
    ficha = models.models.ForeignKey(FormArgeliaFichaAcuerdo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    tipo_identificacion = models.CharField(max_length=50, blank=True, null=True)
    tipo_identificacion_cual = models.CharField(max_length=255, blank=True, null=True)
    numero_identificacion = models.CharField(max_length=50, unique=True, blank=True, null=True)
    parentesco = models.TextField( blank=True, null=True)
    parentesco_otro = models.TextField( blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    estado_civil = models.CharField(max_length=50, blank=True, null=True)
    grupo_especial = models.TextField(default=list, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.numero_identificacion}"