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
    