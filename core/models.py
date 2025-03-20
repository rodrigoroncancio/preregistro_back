from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'core_Rol'

class RolUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="roles")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'core_Rol_Usuario'

class Staff(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    roles = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "%s" % self.user.first_name + " " + self.user.last_name
    
class Campaign(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField( null=True, blank=True)    
    
class SurveyForms(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    survey = models.TextField( null=True, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True, default=1)

class SurveyForms_Privileges(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    survey = models.ForeignKey(SurveyForms, on_delete=models.CASCADE)
    role = models.IntegerField(null=True, blank=True)
    privilege = models.TextField( null=True, blank=True) 
    
class ValidationItems(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    survey = models.TextField(null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True)
    activated = models.BooleanField (default=True) 

class ValidationRegister(models.Model):
    SurveyForms = models.ForeignKey(SurveyForms, on_delete=models.CASCADE, null=True, blank=True)
    validationitems = models.ForeignKey(ValidationItems, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    observation = models.TextField( null=True, blank=True)
    attachment = models.TextField( null=True, blank=True)  
    document_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
    
class ValidationRegister_Logs(models.Model):
    validationregister = models.ForeignKey(ValidationRegister, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True )
    status = models.CharField(max_length=15, null=True, blank=True)
    observation = models.TextField( null=True, blank=True)
    attachment = models.TextField( null=True, blank=True)  
 
 
class ValidationFinalRegister(models.Model):
    SurveyForms = models.ForeignKey(SurveyForms, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    observation = models.TextField( null=True, blank=True)
    attachment = models.TextField( null=True, blank=True)  
    document_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  

class CedulasRnec(models.Model):    
    numero_cedula = models.IntegerField(primary_key=True, db_column='Número de cédula')
    primer_nombre = models.TextField(db_column='Primer Nombre', blank=True, null=True)
    segundo_nombre = models.TextField(db_column='Segundo Nombre', blank=True, null=True)
    primer_apellido = models.TextField(db_column='Primer Apellido', blank=True, null=True)
    segundo_apellido = models.TextField(db_column='Segundo Apellido', blank=True, null=True)
    municipio_expedicion = models.TextField(db_column='Municipio de Expedición del documento', blank=True, null=True)
    departamento_expedicion = models.TextField(db_column='Departamento de Expedición del documento', blank=True, null=True)
    fecha_expedicion = models.TextField(db_column='Fecha de Expedición del documento', blank=True, null=True)
    estado_cedula = models.TextField(db_column='Estado de la Cedula', blank=True, null=True)
    numero_resolucion = models.TextField(db_column='Número de Resolución', blank=True, null=True)
    agno_resolucion = models.TextField(db_column='Año de Resolución', blank=True, null=True)
    genero = models.TextField(db_column='Género', blank=True, null=True)
    fecha_nacimiento = models.TextField(db_column='Fecha de Nacimiento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[report].[Cedulas_RNEC]'

    
class ValidationArgeliaPersonas(models.Model):    
    numero_documento = models.IntegerField(primary_key=True, db_column='NUMERO DOCUMENTO')
    cupo = models.IntegerField(db_column='CUPO', blank=True, null=True)
    nombres = models.TextField(db_column='NOMBRES', blank=True, null=True)
    apellidos = models.TextField(db_column='APELLIDOS', blank=True, null=True)
    telefono = models.TextField(db_column='TELEFONO', blank=True, null=True)
    departamento = models.TextField(db_column='DEPARTAMENTO', blank=True, null=True)
    municipio = models.TextField(db_column='MUNICIPIO', blank=True, null=True)
    corregimiento = models.TextField(db_column='CORREGIMIENTO', blank=True, null=True)
    vereda = models.TextField(db_column='VEREDA', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[report].[V_Argelia_Personas_Validas]'

class Department(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, null=False, blank=False, db_column='Name')
    code = models.CharField(max_length=10, null=False, blank=False, db_column='Code', unique=True)
    active = models.BooleanField(null=True, default=True, db_column='Active')

    class Meta:
        db_table = 'Departments'
        managed = False

class Municipality(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    code = models.CharField(max_length=100, null=False, blank=False, db_column='Code')
    name = models.CharField(max_length=100, null=False, blank=False, db_column='Name')
    departmentid = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='DepartmentId')
    active = models.BooleanField(null=True, default=True, db_column='Active')

    class Meta:
        db_table = 'Municipalities'
        managed = False

class Township(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, null=False, blank=False, db_column='Name')
    municipalityid = models.ForeignKey(Municipality, on_delete=models.DO_NOTHING, db_column='MunicipalityId')

    class Meta:
        db_table = 'Township'
        managed = False

class Village(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, null=False, blank=False, db_column='Name')
    townshipid = models.ForeignKey(Township, on_delete=models.DO_NOTHING, db_column='TownshipId')

    class Meta:
        db_table = 'Village'
        managed = False

class Acquisitionfarm(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, db_column='Name')

    class Meta:
        managed = False
        db_table = 'AcquisitionFarm'

class Civilstatus(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')

    class Meta:
        managed = False
        db_table = 'CivilStatus'

class Condition(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, db_column='Name')

    class Meta:
        managed = False
        db_table = 'Condition'

class Education(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, db_column='Name')

    class Meta:
        managed = False
        db_table = 'Education'

class Familyrelationships(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    titularid = models.IntegerField(null=True, db_column='TitularId')
    beneficiaryid = models.IntegerField(null=True, db_column='BeneficiaryId')
    relationship = models.CharField(max_length=50, null=False, db_column='Relationship')

    class Meta:
        db_table = 'FamilyRelationships'
        managed = False

class Healthaffiliationtype(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, null=False, db_column='Name')

    class Meta:
        db_table = 'HealthAffiliationType'
        managed = False

class Identificationtype(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=50, null=False, db_column='Name')

    class Meta:
        db_table = 'IdentificationType'
        managed = False

class Occupation(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, null=False, db_column='name')

    class Meta:
        db_table = 'Occupation'
        managed = False

class Productiveline(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, null=False, db_column='Name')

    class Meta:
        db_table = 'ProductiveLine'
        managed = False

class Subjectofspecialprotection(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=100, null=False, db_column='Name')

    class Meta:
        db_table = 'SubjectOfSpecialProtection'
        managed = False
        
class PersonaPnis(models.Model):
    identificacion = models.CharField(max_length=100, null=False, db_column='Identificacion')
    nombre = models.CharField(max_length=100, null=False, db_column='Nombre')
    apellido = models.CharField(max_length=100, null=False, db_column='Apellido')

    class Meta:
        db_table = 'Persona_PROD'
        managed = False
        

class UserPNIS(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=255, null=True, blank=True, db_column='Name')
    lastname = models.CharField(max_length=255, null=True, blank=True, db_column='LastName')
    identificationtype = models.ForeignKey('IdentificationType', on_delete=models.SET_NULL, null=True, blank=True, db_column='IdentificationTypeId')
    identificationnumber = models.CharField(max_length=50, null=True, blank=True, db_column='IdentificationNumber')
    gender = models.CharField(max_length=50, null=True, blank=True, db_column='Gender')
    sexualorientation = models.CharField(max_length=50, null=True, blank=True, db_column='SexualOrientation')
    # howtogetfarm = models.TextField(null=True, blank=True, db_column='HowToGetFarm')
    # areacoca = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, db_column='AreaCoca')
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, db_column='Latitude')
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, db_column='Longitude')
    # altitude = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, db_column='Altitude')
    # village = models.ForeignKey('Village', on_delete=models.SET_NULL, null=True, blank=True, db_column='VillageId')
    email = models.EmailField(max_length=255, null=True, blank=True, db_column='Email')
    civilstatusid = models.ForeignKey('CivilStatus', on_delete=models.SET_NULL, null=True, blank=True, db_column='CivilStatusId')
    headofhousehold = models.BooleanField(default=False, db_column='HeadOfHousehold')
    motherheadoffamily = models.BooleanField(default=False, db_column='MotherHeadOfFamily')
    conditionid = models.ForeignKey('Condition', on_delete=models.SET_NULL, null=True, blank=True, db_column='ConditionId')
    occupationid = models.ForeignKey('Occupation', on_delete=models.SET_NULL, null=True, blank=True, db_column='OccupationId')
    educationid = models.ForeignKey('Education', on_delete=models.SET_NULL, null=True, blank=True, db_column='EducationId')
    healthaffiliationtypeid = models.ForeignKey('HealthAffiliationType', on_delete=models.SET_NULL, null=True, blank=True, db_column='HealthAffiliationTypeId')
    subjectofspecialprotectionid = models.ForeignKey('Subjectofspecialprotection', on_delete=models.SET_NULL, null=True, blank=True, db_column='SubjectOfSpecialProtectionId')
    # etniaid = models.IntegerField(null=True, blank=True, db_column='EtniaId')
    communitylocation = models.CharField(max_length=255, null=True, blank=True, db_column='CommunityLocation')
    communityname = models.CharField(max_length=255, null=True, blank=True, db_column='CommunityName')
    etnianame = models.CharField(max_length=255, null=True, blank=True, db_column='EtniaName')
    # registryofyourethniccommunity = models.BooleanField(default=False, db_column='RegistryOfYourEthnicCommunity')
    # productiveprojectislocatedethnicterritory = models.BooleanField(default=False, db_column='ProductiveProjectIsLocatedEthnicTerritory')
    monthlyincome = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='MonthlyIncome')
    monthlyexpenses = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='MonthlyExpenses')
    # department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True, db_column='DepartmentId')
    # municipality = models.ForeignKey('Municipality', on_delete=models.SET_NULL, null=True, blank=True, db_column='MunicipalityId')
    # township = models.ForeignKey('Township', on_delete=models.SET_NULL, null=True, blank=True, db_column='TownshipId')
    propertynamehome = models.CharField(max_length=255, null=True, blank=True, db_column='PropertyNameHome')
    # areahome = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, db_column='AreaHome')
    landcoordinates = models.TextField(null=True, blank=True, db_column='LandCoordinates')
    permanence = models.CharField(max_length=255, null=True, blank=True, db_column='Permanence')
    # acquisitionhome = models.ForeignKey('Acquisitionfarm', on_delete=models.SET_NULL, null=True, blank=True, db_column='AcquisitionHomeId')
    # documentacquisitionhome = models.CharField(max_length=255, null=True, blank=True, db_column='DocumentAcquisitionHome')
    # dependents = models.PositiveIntegerField(null=True, blank=True, db_column='Dependents')
    # minorsinfamily = models.PositiveIntegerField(null=True, blank=True, db_column='MinorsInFamily')
    # acquisitionhomeidentificationtypeid = models.IntegerField(null=True, blank=True, db_column='AcquisitionHomeIdentificationTypeId')
    acquisitionhomeidentificationnumber = models.CharField(max_length=50, null=True, blank=True, db_column='AcquisitionHomeIdentificationNumber')
    landownership = models.CharField(max_length=255, null=True, blank=True, db_column='LandOwnership')
    # departmentfarmid = models.IntegerField(null=True, blank=True, db_column='DepartmentFarmId')
    # municipalityfarmid = models.IntegerField(null=True, blank=True, db_column='MunicipalityFarmId')
    # townshipfarmid = models.IntegerField(null=True, blank=True, db_column='TownshipFarmId')
    # villagefarmid = models.IntegerField(null=True, blank=True, db_column='VillageFarmId')
    # acquisitionfarmid = models.IntegerField(null=True, blank=True, db_column='AcquisitionFarmId')
    propertynamefarm = models.CharField(max_length=255, null=True, blank=True, db_column='PropertyNameFarm')
    # areafarm = models.FloatField(null=True, blank=True, db_column='AreaFarm')
    landcoordinates2 = models.CharField(max_length=255, null=True, blank=True, db_column='LandCoordinates2')
    # documentacquisitionfarm = models.CharField(max_length=255, null=True, blank=True, db_column='DocumentAcquisitionFarm')
    # acquisitionfarmidentificationtypeid = models.IntegerField(null=True, blank=True, db_column='AcquisitionFarmIdentificationTypeId')
    acquisitionfarmidentificationnumber = models.CharField(max_length=50, null=True, blank=True, db_column='AcquisitionFarmIdentificationNumber')
    # rootedtomunicipality = models.BooleanField(default=False, db_column='RootedToMunicipality')
    landrelationshiptype = models.CharField(max_length=255, null=True, blank=True, db_column='LandRelationshipType')
    landdocumenttype = models.CharField(max_length=255, null=True, blank=True, db_column='LandDocumentType')
    landownername = models.CharField(max_length=255, null=True, blank=True, db_column='LandOwnerName')
    # residentsonland = models.PositiveIntegerField(null=True, blank=True, db_column='ResidentsOnLand')
    # haslegalactivities = models.BooleanField(default=False, db_column='HasLegalActivities')
    # LegalActivitiesid = models.IntegerField(null=True, blank=True, db_column='LegalActivitiesId')
    # familyexclusiveusage = models.BooleanField(default=False, db_column='FamilyExclusiveUsage')
    # familyotherlands = models.BooleanField(default=False, db_column='FamilyOtherLands')
    # productiveline = models.ForeignKey('ProductiveLine', on_delete=models.SET_NULL, null=True, blank=True, db_column='ProductiveLineId')
    establishment = models.CharField(max_length=255, null=True, blank=True, db_column='Establishment')
    strengthening = models.CharField(max_length=255, null=True, blank=True, db_column='Strengthening')
    signature = models.TextField(null=True, blank=True, db_column='Signature')
    reservation_name = models.CharField(max_length=255, null=True, blank=True, db_column='ReservationName')
    # accreditation_document_pdf = models.FileField(upload_to='documents/', null=True, blank=True, db_column='AccreditationDocumentPdf')
    economicactivity = models.CharField(max_length=255, null=True, blank=True, db_column='EconomicActivity')
    experienceproductionline = models.CharField(max_length=255, null=True, blank=True, db_column='ExperienceProductionLine')
    # yearsexperienceproductionline = models.IntegerField(null=True, blank=True, db_column='YearsExperienceProductionLine')

    class Meta:
        ordering = ('id',)
        db_table = 'Users'  # Asegura que el modelo apunte a la tabla existente en SQL Server
        managed = False  # Evita que Django intente modificar la tabla

class ArgeliaGrupos(models.Model):
    id = models.CharField(max_length=41, primary_key=True, db_column='__id')
    cub = models.IntegerField(null=True, blank=True, db_column='CUB_ASOCIACION')
    linea_productiva = models.TextField(null=True, blank=True, db_column='LINEA PRODUCTIVA')
    experiencia_linea_productiva = models.TextField(null=True, blank=True, db_column='EXPERIENCIA LINEA PRODUCTIVA')
    experiencia_linea_productiva_agnos = models.TextField(null=True, blank=True, db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS')
    fecha = models.TextField(null=True, blank=True, db_column='FECHA')
    grupo_pruductores = models.TextField(null=True, blank=True, db_column='GRUPO PRUDUCTORES')
    tipo_organizacion = models.TextField(null=True, blank=True, db_column='TIPO ORGANIZACION')
    tipo_organizacion_cual = models.TextField(null=True, blank=True, db_column='TIPO ORGANIZACION CUAL')
    identificacion_organizacion = models.TextField(null=True, blank=True, db_column='IDENTIFICACION ORGANIZACION')
    representante = models.TextField(null=True, blank=True, db_column='REPRESENTANTE')
    cedula_representante = models.TextField(null=True, blank=True, db_column='CEDULA REPRESENTANTE')
    telefono = models.TextField(null=True, blank=True, db_column='TELEFONO')
    correo = models.TextField(null=True, blank=True, db_column='CORREO')
    departamento_influencia = models.TextField(null=True, blank=True, db_column='DEPARTAMENTO INFLUENCIA')
    municipio_influencia = models.TextField(null=True, blank=True, db_column='MUNICIPIO INFLUENCIA')
    vereda_influencia = models.TextField(null=True, blank=True, db_column='VEREDA INFLUENCIA')
    fecha_creacion = models.TextField(null=True, blank=True, db_column='FECHA CREACION')
    principales_lineas_productivas = models.TextField(null=True, blank=True, db_column='PRINCIPALES LINEAS PRODUCTIVAS')
    principales_lineas_productivas_cual = models.TextField(null=True, blank=True, db_column='PRINCIPALES LINEAS PRODUCTIVAS CUAL')
    departamento = models.TextField(null=True, blank=True, db_column='DEPARTAMENTO')
    municipio = models.TextField(null=True, blank=True, db_column='MUNICIPIO')
    numero_familias_grupo_pruductores = models.TextField(null=True, blank=True, db_column='NUMERO FAMILIAS GRUPO PRUDUCTORES')
    num_personas_registradas = models.IntegerField(null=True, blank=True, db_column='NUM_PERSONAS_REGISTRADAS')

    class Meta:
        ordering = ('cub',)
        db_table = '[stg].[V_Argelia_Encuesta_Grupo]'  # Asegura que el modelo apunte a la tabla existente en SQL Server
        managed = False  # Evita que Django intente modificar la tabla

class ArgeliaPersonas(models.Model):
    id = models.CharField(max_length=41, primary_key=True, db_column='id')
    submissiondate = models.TextField(db_column='SUBMISSIONDATE', null=True, blank=True)
    updatedat = models.TextField(db_column='UPDATEDAT', null=True, blank=True)
    submitterid = models.TextField(db_column='SUBMITTERID', null=True, blank=True)
    submittername = models.TextField(db_column='SUBMITTERNAME', null=True, blank=True)
    attachmentspresent = models.TextField(db_column='ATTACHMENTSPRESENT', null=True, blank=True)
    attachmentsexpected = models.TextField(db_column='ATTACHMENTSEXPECTED', null=True, blank=True)
    status = models.TextField(db_column='STATUS', null=True, blank=True)
    reviewstate = models.TextField(db_column='REVIEWSTATE', null=True, blank=True)
    deviceid = models.TextField(db_column='DEVICEID', null=True, blank=True)
    edits = models.TextField(db_column='EDITS', null=True, blank=True)
    formversion = models.TextField(db_column='FORMVERSION', null=True, blank=True)
    nota1 = models.TextField(db_column='NOTA1', null=True, blank=True)
    nota7 = models.TextField(db_column='NOTA7', null=True, blank=True)
    identificacion = models.TextField(db_column='IDENTIFICACION', null=True, blank=True)
    validacionidentificacion = models.TextField(db_column='VALIDACION IDENTIFICACION', null=True, blank=True)
    identificacionvalida = models.TextField(db_column='IDENTIFICACION VALIDA', null=True, blank=True)
    fecha = models.TextField(db_column='FECHA', null=True, blank=True)
    codigofamiliasencuesta = models.TextField(db_column='CODIGO FAMILIAS ENCUESTA', null=True, blank=True)
    validacioncodigofamiliasencuesta = models.TextField(db_column='VALIDACION CODIGO FAMILIAS ENCUESTA', null=True, blank=True)
    codigofamiliasencuestavalida1 = models.TextField(db_column='CODIGO FAMILIAS ENCUESTA VALIDA1', null=True, blank=True)
    codigofamiliasencuestavalida = models.TextField(db_column='CODIGO FAMILIAS ENCUESTA VALIDA', null=True, blank=True)
    lineaproductiva = models.TextField(db_column='LINEA PRODUCTIVA', null=True, blank=True)
    nota2 = models.TextField(db_column='NOTA2', null=True, blank=True)
    nombres = models.TextField(db_column='NOMBRES', null=True, blank=True)
    apellidos = models.TextField(db_column='APELLIDOS', null=True, blank=True)
    tipodocumento = models.TextField(db_column='TIPO DOCUMENTO', null=True, blank=True)
    numerodocumento = models.TextField(db_column='NUMERO DOCUMENTO', null=True, blank=True)
    documentovalido = models.TextField(db_column='DOCUMENTO VALIDO', null=True, blank=True)
    fotodocumentofrente = models.TextField(db_column='FOTO DOCUMENTO FRENTE', null=True, blank=True)
    fotodocumentorespaldo = models.TextField(db_column='FOTO DOCUMENTO RESPALDO', null=True, blank=True)
    fechanacimiento = models.TextField(db_column='FECHA NACIMIENTO', null=True, blank=True)
    edad = models.TextField(db_column='EDAD', null=True, blank=True)
    sexo = models.TextField(db_column='SEXO', null=True, blank=True)
    madrecabezafamilia = models.TextField(db_column='MADRE CABEAZA FAMILIA', null=True, blank=True)
    orientacion = models.TextField(db_column='ORIENTACION', null=True, blank=True)
    telefono = models.TextField(db_column='TELEFONO', null=True, blank=True)
    correo = models.TextField(db_column='CORREO', null=True, blank=True)
    tipociudadano = models.TextField(db_column='TIPO CIUDADANO', null=True, blank=True)
    condicion = models.TextField(db_column='CONDICION', null=True, blank=True)
    discapacidad = models.TextField(db_column='DISCAPACIDAD', null=True, blank=True)
    educacion = models.TextField(db_column='EDUCACION', null=True, blank=True)
    numeropersonas = models.TextField(db_column='NUMERO PERSONAS', null=True, blank=True)
    departamento = models.TextField(db_column='DEPARTAMENTO', null=True, blank=True)
    municipio = models.TextField(db_column='MUNICIPIO', null=True, blank=True)
    descripcionacceso = models.TextField(db_column='DESCRIPCION ACCESO', null=True, blank=True)
    predio = models.TextField(db_column='PREDIO', null=True, blank=True)
    areapredio = models.TextField(db_column='AREA PREDIO', null=True, blank=True)
    areacoca = models.TextField(db_column='AREA COCA', null=True, blank=True)
    tenencia = models.TextField(db_column='TENENCIA', null=True, blank=True)
    fototenencia = models.TextField(db_column='FOTO TENENCIA', null=True, blank=True)
    coordenadas = models.TextField(db_column='COORDENADAS', null=True, blank=True)
    residenciapredio = models.TextField(db_column='RESIDENCIA PREDIO', null=True, blank=True)
    usufructuaotropredio = models.TextField(db_column='USUFRUCTUA OTRO PREDIO', null=True, blank=True)
    actividadeconomicaotropredio = models.TextField(db_column='ACTIVIDAD ECONOMICA OTRO PREDIO', null=True, blank=True)
    experiencialineaproductiva = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA', null=True, blank=True)
    experiencialineaproductivaanos = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS', null=True, blank=True)
    lecturaterminos = models.TextField(db_column='LECTURA TERMINOS', null=True, blank=True)
    lecturatratamiento_datos = models.TextField(db_column='LECTURA TRATAMIENTO DATOS', null=True, blank=True)
    instanceid = models.TextField(db_column='INSTANCEID', null=True, blank=True)

    class Meta:
        db_table = '[stg].[Argelia_Personas]'  # Asegura que el modelo apunte a la tabla existente en SQL Server
        managed = False  # Evita que Django intente modificar la tabla

class ArgeliaPersonasValidadas(models.Model):
    numero_identificacion = models.TextField(db_column='NUMERO DOCUMENTO', null=True, blank=True)
    nombres = models.TextField(db_column='NOMBRES', null=True, blank=True)
    apellidos = models.TextField(db_column='APELLIDOS', null=True, blank=True)
        
    class Meta:
        db_table = '[report].[V_Argelia_Personas_Validas]'
        managed = False  # Evita que Django intente modificar la tabla     
        
class CatatumboPersonasValidadas(models.Model):
    numero_identificacion = models.TextField(db_column='NUMERO DOCUMENTO', null=True, blank=True)
    nombres = models.TextField(db_column='NOMBRES', null=True, blank=True)
    apellidos = models.TextField(db_column='APELLIDOS', null=True, blank=True)
        
    class Meta:
        db_table = '[report].[V_Catatumbo_Personas_Validas]'
        managed = False  # Evita que Django intente modificar la tabla  
        
class NucleoFamiliarPersonas(models.Model):
    titular_identificacion = models.TextField(db_column='titular_identificacion', null=True, blank=True)
    beneficiario_identificationNumber = models.TextField(db_column='beneficiario_identificationnumber', null=True, blank=True)
    beneficiario_nombre = models.TextField(db_column='beneficiario_nombre', null=True, blank=True)
    beneficiario_apellido = models.TextField(db_column='beneficiario_apellido', null=True, blank=True)
    estado_civil = models.TextField(db_column='estado_civil', null=True, blank=True)
    Birthdate = models.TextField(db_column='Birthdate', null=True, blank=True)
    especial = models.TextField(db_column='especial', null=True, blank=True)
    parentesco = models.TextField(db_column='Relationship', null=True, blank=True)
        
    class Meta:
        db_table = '[dbo].[V_NucleoFamiliar]'
        managed = False  # Evita que Django intente modificar la tabla             

class CatatumboIndividuales(models.Model):
    id = models.CharField(max_length=41, primary_key=True, db_column='__id')
    fase = models.TextField(db_column='FASE', null=True, blank=True)
    submission_date = models.TextField(db_column='SUBMISSIONDATE', null=True, blank=True)
    updated_at = models.TextField(db_column='UPDATEDAT', null=True, blank=True)
    submitter_id = models.TextField(db_column='SUBMITTERID', null=True, blank=True)
    submitter_name = models.TextField(db_column='SUBMITTERNAME', null=True, blank=True)
    attachments_present = models.TextField(db_column='ATTACHMENTSPRESENT', null=True, blank=True)
    attachments_expected = models.TextField(db_column='ATTACHMENTSEXPECTED', null=True, blank=True)
    status = models.TextField(db_column='STATUS', null=True, blank=True)
    review_state = models.TextField(db_column='REVIEWSTATE', null=True, blank=True)
    device_id = models.TextField(db_column='DEVICEID', null=True, blank=True)
    edits = models.TextField(db_column='EDITS', null=True, blank=True)
    form_version = models.TextField(db_column='FORMVERSION', null=True, blank=True)
    nota1 = models.TextField(db_column='NOTA1', null=True, blank=True)
    nota7 = models.TextField(db_column='NOTA7', null=True, blank=True)
    tiene_coca = models.TextField(db_column='TIENE COCA', null=True, blank=True)
    identificacion = models.TextField(db_column='IDENTIFICACION', null=True, blank=True)
    validacion_identificacion_pnis = models.TextField(db_column='VALIDACION IDENTIFICACION PNIS', null=True, blank=True)
    identificacion_valida_pnis = models.TextField(db_column='IDENTIFICACION VALIDA PNIS', null=True, blank=True)
    validacion_identificacion_proveedores = models.TextField(db_column='VALIDACION IDENTIFICACION PROVEEDORES', null=True, blank=True)
    identificacion_valida_proveedores = models.TextField(db_column='IDENTIFICACION VALIDA PROVEEDORES', null=True, blank=True)
    validacion_identificacion_inscritos = models.TextField(db_column='VALIDACION IDENTIFICACION INSCRITOS', null=True, blank=True)
    identificacion_valida_inscritos = models.TextField(db_column='IDENTIFICACION VALIDA INSCRITOS', null=True, blank=True)
    victima_posterior_2025 = models.TextField(db_column='VICTIMA POSTERIOR 2025', null=True, blank=True)
    fecha = models.TextField(db_column='FECHA', null=True, blank=True)
    fecha_nacimiento = models.TextField(db_column='FECHA NACIMIENTO', null=True, blank=True)
    tipo_linea_productiva = models.TextField(db_column='TIPO LINEA PRODUCTIVA', null=True, blank=True)
    condicion_linea_productiva = models.TextField(db_column='CONDICION LINEA PRODUCTIVA', null=True, blank=True)
    linea_productiva = models.TextField(db_column='LINEA PRODUCTIVA', null=True, blank=True)
    linea_productiva_fortalecimiento = models.TextField(db_column='LINEA PRODUCTIVA FORTALECIMIENTO', null=True, blank=True)
    linea_productiva_fortalecimiento_cual = models.TextField(db_column='LINEA PRODUCTIVA FORTALECIMIENTO CUAL', null=True, blank=True)
    experiencia_linea_productiva = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA', null=True, blank=True)
    experiencia_linea_productiva_anos = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS', null=True, blank=True)
    ha_sembradas = models.TextField(db_column='HA SEMBRADAS', null=True, blank=True)
    volumen_produccion = models.TextField(db_column='VOLUMEN PRODUCCION', null=True, blank=True)
    condicion_linea_productiva_no_agropecuaria = models.TextField(db_column='CONDICION LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    linea_productiva_no_agropecuaria = models.TextField(db_column='LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    experiencia_linea_productiva_no_agropecuaria = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    experiencia_linea_productiva_anos_no_agropecuaria = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS NO AGROPECUARIA', null=True, blank=True)
    formacion_linea_productiva_no_agropecuaria = models.TextField(db_column='FORMACION LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    formacion_linea_productiva_no_agropecuaria_cual = models.TextField(db_column='FORMACION LINEA PRODUCTIVA NO AGROPECUARIA CUAL', null=True, blank=True)
    departamento_proyecto_productivo_victima = models.TextField(db_column='DEPARTAMENTO PROYECTO PRODUCTIVO VICTIMA', null=True, blank=True)
    municipio_proyecto_productivo_victima = models.TextField(db_column='MUNICIPIO PROYECTO PRODUCTIVO VICTIMA', null=True, blank=True)
    centro_poblado_proyecto_productivo = models.TextField(db_column='CENTRO POBLADO PROYECTO PRODUCTIVO', null=True, blank=True)
    descripcion_acceso_proyecto_productivo_victima = models.TextField(db_column='DESCRIPCION ACCESO PROYECTO PRODUCTIVO VICTIMA', null=True, blank=True)
    departamento_proyecto_productivo = models.TextField(db_column='DEPARTAMENTO PROYECTO PRODUCTIVO', null=True, blank=True)
    municipio_proyecto_productivo = models.TextField(db_column='MUNICIPIO PROYECTO PRODUCTIVO', null=True, blank=True)
    vereda_proyecto_productivo = models.TextField(db_column='VEREDA PROYECTO PRODUCTIVO', null=True, blank=True)
    descripcion_acceso_proyecto_productivo = models.TextField(db_column='DESCRIPCION ACCESO PROYECTO PRODUCTIVO', null=True, blank=True)
    nombres = models.TextField(db_column='NOMBRES', null=True, blank=True)
    apellidos = models.TextField(db_column='APELLIDOS', null=True, blank=True)
    tipo_documento = models.TextField(db_column='TIPO DOCUMENTO', null=True, blank=True)
    numero_documento = models.TextField(db_column='NUMERO DOCUMENTO', null=True, blank=True)
    documento_valido = models.TextField(db_column='DOCUMENTO VALIDO', null=True, blank=True)
    foto_documento_frente = models.TextField(db_column='FOTO DOCUMENTO FRENTE', null=True, blank=True)
    foto_documento_respaldo = models.TextField(db_column='FOTO DOCUMENTO RESPALDO', null=True, blank=True)
    madre_cabeza_familia = models.CharField(max_length=255, db_column='MADRE CABEAZA FAMILIA', null=True, blank=True)
    orientacion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    correo = models.CharField(max_length=255, null=True, blank=True)
    tipo_ciudadano = models.CharField(max_length=255, db_column='TIPO CIUDADANO', null=True, blank=True)
    pueblo = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.CharField(max_length=255, db_column='SEXO', null=True, blank=True)
    etnico = models.CharField(max_length=255, db_column='ETNICO', null=True, blank=True)
    nombre_comunidad = models.CharField(max_length=255, db_column='NOMBRECOMUNIDAD', null=True, blank=True)
    censo = models.CharField(max_length=255, null=True, blank=True)
    nombre_comunidad1 = models.CharField(max_length=255, db_column='NOMBRECOMUNIDAD1', null=True, blank=True)
    lote_etnico = models.CharField(max_length=255, db_column='LOTEETNICO', null=True, blank=True)
    condicion = models.CharField(max_length=255, db_column='CONDICION', null=True, blank=True)
    discapacidad = models.CharField(max_length=255, db_column='DISCAPACIDAD', null=True, blank=True)
    educacion = models.CharField(max_length=255, db_column='EDUCACION', null=True, blank=True)
    numero_personas = models.CharField(max_length=255, db_column='NUMERO PERSONAS', null=True, blank=True)
    numero_documentos_personas_nucleo = models.CharField(max_length=255, db_column='NUMERO DOCUMENTOS PERSONAS NUCLEO', null=True, blank=True)
    nombres_documentos_personas_nucleo = models.CharField(max_length=255, db_column='NOMBRES DOCUMENTOS PERSONAS NUCLEO', null=True, blank=True)
    numero_total_predios_inscribir = models.CharField(max_length=255, db_column='NUMERO TOTAL PREDIOS INSCRIBIR', null=True, blank=True)
    numero_predios_inscribir = models.CharField(max_length=255, db_column='NUMERO PREDIOS INSCRIBIR', null=True, blank=True)
    departamento = models.CharField(max_length=255, db_column='DEPARTAMENTO', null=True, blank=True)
    municipio = models.TextField(max_length=255, db_column='MUNICIPIO', null=True, blank=True)
    vereda = models.TextField(db_column='VEREDA', null=True, blank=True)
    vereda_cual = models.TextField(db_column='VEREDA CUAL', null=True, blank=True)
    descripcion_acceso = models.TextField(db_column='DESCRIPCION ACCESO', null=True, blank=True)
    predio = models.TextField(db_column='PREDIO', null=True, blank=True)
    area_predio = models.TextField(db_column='AREA PREDIO', null=True, blank=True)
    area_coca = models.TextField(db_column='AREA COCA', null=True, blank=True)
    tenencia = models.TextField(db_column='TENENCIA', null=True, blank=True)
    coordenadas = models.TextField(db_column='COORDENADAS', null=True, blank=True)
    
    municipiop2 = models.TextField(max_length=255, db_column='MUNICIPIO P2', null=True, blank=True)
    veredap2 = models.TextField(db_column='VEREDA P2', null=True, blank=True)
    vereda_cualp2 = models.TextField(db_column='VEREDA CUAL P2', null=True, blank=True)
    descripcion_accesop2 = models.TextField(db_column='DESCRIPCION ACCESO P2', null=True, blank=True)
    prediop2 = models.TextField(db_column='PREDIO P2', null=True, blank=True)
    area_prediop2 = models.TextField(db_column='AREA PREDIO P2', null=True, blank=True)
    area_cocap2 = models.TextField(db_column='AREA COCA P2', null=True, blank=True)
    tenenciap2 = models.TextField(db_column='TENENCIA P2', null=True, blank=True)
    coordenadasp2 = models.TextField(db_column='COORDENADAS P2', null=True, blank=True)
    
    municipiop3 = models.TextField(max_length=255, db_column='MUNICIPIO P3', null=True, blank=True)
    veredap3 = models.TextField(db_column='VEREDA P3', null=True, blank=True)
    vereda_cualp3 = models.TextField(db_column='VEREDA CUAL P3', null=True, blank=True)
    descripcion_accesop3 = models.TextField(db_column='DESCRIPCION ACCESO P3', null=True, blank=True)
    prediop3 = models.TextField(db_column='PREDIO P3', null=True, blank=True)
    area_prediop3 = models.TextField(db_column='AREA PREDIO P3', null=True, blank=True)
    area_cocap3 = models.TextField(db_column='AREA COCA P3', null=True, blank=True)
    tenenciap3 = models.TextField(db_column='TENENCIA P3', null=True, blank=True)
    coordenadasp3 = models.TextField(db_column='COORDENADAS P3', null=True, blank=True)
    

    departamento_residencia = models.TextField(db_column='DEPARTAMENTO RESIDENCIA', null=True, blank=True)
    municipio_residencia = models.TextField(db_column='MUNICIPIO RESIDENCIA', null=True, blank=True)
    vereda_residencia = models.TextField(db_column='VEREDA RESIDENCIA', null=True, blank=True)
    descripcion_residencia = models.TextField(db_column='DESCRIPCION ACCESO_', null=True, blank=True)
    predio_residencia = models.TextField(db_column='PREDIO RESIDENCIA', null=True, blank=True)
    usufructa_predio = models.TextField(db_column='USUFRUCTUA OTRO PREDIO', null=True, blank=True)
    actividad_econo_otro = models.TextField(db_column='ACTIVIDAD ECONOMICA OTRO PREDIO', null=True, blank=True)
        
    class Meta:
        db_table = '[stg].[Catatumbo_Individuales]'
        managed = False  # Evita que Django intente modificar la tabla    

class VCatatumboIndividuales(models.Model):
    id = models.CharField(max_length=41, primary_key=True, db_column='__id')
    fase = models.TextField(db_column='FASE', null=True, blank=True)
    submission_date = models.TextField(db_column='SUBMISSIONDATE', null=True, blank=True)
    updated_at = models.TextField(db_column='UPDATEDAT', null=True, blank=True)
    submitter_id = models.TextField(db_column='SUBMITTERID', null=True, blank=True)
    submitter_name = models.TextField(db_column='SUBMITTERNAME', null=True, blank=True)
    attachments_present = models.TextField(db_column='ATTACHMENTSPRESENT', null=True, blank=True)
    attachments_expected = models.TextField(db_column='ATTACHMENTSEXPECTED', null=True, blank=True)
    status = models.TextField(db_column='STATUS', null=True, blank=True)
    review_state = models.TextField(db_column='REVIEWSTATE', null=True, blank=True)
    device_id = models.TextField(db_column='DEVICEID', null=True, blank=True)
    edits = models.TextField(db_column='EDITS', null=True, blank=True)
    form_version = models.TextField(db_column='FORMVERSION', null=True, blank=True)
    nota1 = models.TextField(db_column='NOTA1', null=True, blank=True)
    nota7 = models.TextField(db_column='NOTA7', null=True, blank=True)
    tiene_coca = models.TextField(db_column='TIENE COCA', null=True, blank=True)
    identificacion = models.TextField(db_column='IDENTIFICACION', null=True, blank=True)
    validacion_identificacion_pnis = models.TextField(db_column='VALIDACION IDENTIFICACION PNIS', null=True, blank=True)
    identificacion_valida_pnis = models.TextField(db_column='IDENTIFICACION VALIDA PNIS', null=True, blank=True)
    validacion_identificacion_proveedores = models.TextField(db_column='VALIDACION IDENTIFICACION PROVEEDORES', null=True, blank=True)
    identificacion_valida_proveedores = models.TextField(db_column='IDENTIFICACION VALIDA PROVEEDORES', null=True, blank=True)
    validacion_identificacion_inscritos = models.TextField(db_column='VALIDACION IDENTIFICACION INSCRITOS', null=True, blank=True)
    identificacion_valida_inscritos = models.TextField(db_column='IDENTIFICACION VALIDA INSCRITOS', null=True, blank=True)
    victima_posterior_2025 = models.TextField(db_column='VICTIMA POSTERIOR 2025', null=True, blank=True)
    fecha = models.TextField(db_column='FECHA', null=True, blank=True)
    fecha_nacimiento = models.TextField(db_column='FECHA NACIMIENTO', null=True, blank=True)
    tipo_linea_productiva = models.TextField(db_column='TIPO LINEA PRODUCTIVA', null=True, blank=True)
    condicion_linea_productiva = models.TextField(db_column='CONDICION LINEA PRODUCTIVA', null=True, blank=True)
    linea_productiva = models.TextField(db_column='LINEA PRODUCTIVA', null=True, blank=True)
    linea_productiva_fortalecimiento = models.TextField(db_column='LINEA PRODUCTIVA FORTALECIMIENTO', null=True, blank=True)
    linea_productiva_fortalecimiento_cual = models.TextField(db_column='LINEA PRODUCTIVA FORTALECIMIENTO CUAL', null=True, blank=True)
    experiencia_linea_productiva = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA', null=True, blank=True)
    experiencia_linea_productiva_anos = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS', null=True, blank=True)
    ha_sembradas = models.TextField(db_column='HA SEMBRADAS', null=True, blank=True)
    volumen_produccion = models.TextField(db_column='VOLUMEN PRODUCCION', null=True, blank=True)
    condicion_linea_productiva_no_agropecuaria = models.TextField(db_column='CONDICION LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    linea_productiva_no_agropecuaria = models.TextField(db_column='LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    experiencia_linea_productiva_no_agropecuaria = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    experiencia_linea_productiva_anos_no_agropecuaria = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS NO AGROPECUARIA', null=True, blank=True)
    formacion_linea_productiva_no_agropecuaria = models.TextField(db_column='FORMACION LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    formacion_linea_productiva_no_agropecuaria_cual = models.TextField(db_column='FORMACION LINEA PRODUCTIVA NO AGROPECUARIA CUAL', null=True, blank=True)
    departamento_proyecto_productivo_victima = models.TextField(db_column='DEPARTAMENTO PROYECTO PRODUCTIVO VICTIMA', null=True, blank=True)
    municipio_proyecto_productivo_victima = models.TextField(db_column='MUNICIPIO PROYECTO PRODUCTIVO VICTIMA', null=True, blank=True)
    centro_poblado_proyecto_productivo = models.TextField(db_column='CENTRO POBLADO PROYECTO PRODUCTIVO', null=True, blank=True)
    descripcion_acceso_proyecto_productivo_victima = models.TextField(db_column='DESCRIPCION ACCESO PROYECTO PRODUCTIVO VICTIMA', null=True, blank=True)
    departamento_proyecto_productivo = models.TextField(db_column='DEPARTAMENTO PROYECTO PRODUCTIVO', null=True, blank=True)
    municipio_proyecto_productivo = models.TextField(db_column='MUNICIPIO PROYECTO PRODUCTIVO', null=True, blank=True)
    vereda_proyecto_productivo = models.TextField(db_column='VEREDA PROYECTO PRODUCTIVO', null=True, blank=True)
    descripcion_acceso_proyecto_productivo = models.TextField(db_column='DESCRIPCION ACCESO PROYECTO PRODUCTIVO', null=True, blank=True)
    nombres = models.TextField(db_column='NOMBRES', null=True, blank=True)
    apellidos = models.TextField(db_column='APELLIDOS', null=True, blank=True)
    tipo_documento = models.TextField(db_column='TIPO DOCUMENTO', null=True, blank=True)
    numero_documento = models.TextField(db_column='NUMERO DOCUMENTO', null=True, blank=True)
    documento_valido = models.TextField(db_column='DOCUMENTO VALIDO', null=True, blank=True)
    foto_documento_frente = models.TextField(db_column='FOTO DOCUMENTO FRENTE', null=True, blank=True)
    foto_documento_respaldo = models.TextField(db_column='FOTO DOCUMENTO RESPALDO', null=True, blank=True)
    madre_cabeza_familia = models.CharField(max_length=255, db_column='MADRE CABEAZA FAMILIA', null=True, blank=True)
    orientacion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    correo = models.CharField(max_length=255, null=True, blank=True)
    tipo_ciudadano = models.CharField(max_length=255, db_column='TIPO CIUDADANO', null=True, blank=True)
    pueblo = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.CharField(max_length=255, db_column='SEXO', null=True, blank=True)
    etnico = models.CharField(max_length=255, db_column='ETNICO', null=True, blank=True)
    nombre_comunidad = models.CharField(max_length=255, db_column='NOMBRECOMUNIDAD', null=True, blank=True)
    censo = models.CharField(max_length=255, null=True, blank=True)
    nombre_comunidad1 = models.CharField(max_length=255, db_column='NOMBRECOMUNIDAD1', null=True, blank=True)
    lote_etnico = models.CharField(max_length=255, db_column='LOTEETNICO', null=True, blank=True)
    condicion = models.CharField(max_length=255, db_column='CONDICION', null=True, blank=True)
    discapacidad = models.CharField(max_length=255, db_column='DISCAPACIDAD', null=True, blank=True)
    educacion = models.CharField(max_length=255, db_column='EDUCACION', null=True, blank=True)
    numero_personas = models.CharField(max_length=255, db_column='NUMERO PERSONAS', null=True, blank=True)
    numero_documentos_personas_nucleo = models.CharField(max_length=255, db_column='NUMERO DOCUMENTOS PERSONAS NUCLEO', null=True, blank=True)
    nombres_documentos_personas_nucleo = models.CharField(max_length=255, db_column='NOMBRES DOCUMENTOS PERSONAS NUCLEO', null=True, blank=True)
    numero_total_predios_inscribir = models.CharField(max_length=255, db_column='NUMERO TOTAL PREDIOS INSCRIBIR', null=True, blank=True)
    numero_predios_inscribir = models.CharField(max_length=255, db_column='NUMERO PREDIOS INSCRIBIR', null=True, blank=True)
    departamento = models.CharField(max_length=255, db_column='DEPARTAMENTO', null=True, blank=True)
    municipio = models.TextField(max_length=255, db_column='MUNICIPIO', null=True, blank=True)
    vereda = models.TextField(db_column='VEREDA', null=True, blank=True)
    vereda_cual = models.TextField(db_column='VEREDA CUAL', null=True, blank=True)
    descripcion_acceso = models.TextField(db_column='DESCRIPCION ACCESO', null=True, blank=True)
    predio = models.TextField(db_column='PREDIO', null=True, blank=True)
    area_predio = models.TextField(db_column='AREA PREDIO', null=True, blank=True)
    area_coca = models.TextField(db_column='AREA COCA', null=True, blank=True)
    tenencia = models.TextField(db_column='TENENCIA', null=True, blank=True)
    coordenadas = models.TextField(db_column='COORDENADAS', null=True, blank=True)
    
    municipiop2 = models.TextField(max_length=255, db_column='MUNICIPIO P2', null=True, blank=True)
    veredap2 = models.TextField(db_column='VEREDA P2', null=True, blank=True)
    vereda_cualp2 = models.TextField(db_column='VEREDA CUAL P2', null=True, blank=True)
    descripcion_accesop2 = models.TextField(db_column='DESCRIPCION ACCESO P2', null=True, blank=True)
    prediop2 = models.TextField(db_column='PREDIO P2', null=True, blank=True)
    area_prediop2 = models.TextField(db_column='AREA PREDIO P2', null=True, blank=True)
    area_cocap2 = models.TextField(db_column='AREA COCA P2', null=True, blank=True)
    tenenciap2 = models.TextField(db_column='TENENCIA P2', null=True, blank=True)
    coordenadasp2 = models.TextField(db_column='COORDENADAS P2', null=True, blank=True)
    
    municipiop3 = models.TextField(max_length=255, db_column='MUNICIPIO P3', null=True, blank=True)
    veredap3 = models.TextField(db_column='VEREDA P3', null=True, blank=True)
    vereda_cualp3 = models.TextField(db_column='VEREDA CUAL P3', null=True, blank=True)
    descripcion_accesop3 = models.TextField(db_column='DESCRIPCION ACCESO P3', null=True, blank=True)
    prediop3 = models.TextField(db_column='PREDIO P3', null=True, blank=True)
    area_prediop3 = models.TextField(db_column='AREA PREDIO P3', null=True, blank=True)
    area_cocap3 = models.TextField(db_column='AREA COCA P3', null=True, blank=True)
    tenenciap3 = models.TextField(db_column='TENENCIA P3', null=True, blank=True)
    coordenadasp3 = models.TextField(db_column='COORDENADAS P3', null=True, blank=True)
    
    departamento_residencia = models.TextField(db_column='DEPARTAMENTO RESIDENCIA', null=True, blank=True)
    municipio_residencia = models.TextField(db_column='MUNICIPIO RESIDENCIA', null=True, blank=True)
    vereda_residencia = models.TextField(db_column='VEREDA RESIDENCIA', null=True, blank=True)
    descripcion_residencia = models.TextField(db_column='DESCRIPCION ACCESO_', null=True, blank=True)
    predio_residencia = models.TextField(db_column='PREDIO RESIDENCIA', null=True, blank=True)
    usufructa_predio = models.TextField(db_column='USUFRUCTUA OTRO PREDIO', null=True, blank=True)
    actividad_econo_otro = models.TextField(db_column='ACTIVIDAD ECONOMICA OTRO PREDIO', null=True, blank=True)
    validado_final = models.TextField(db_column='validado_final', null=True, blank=True)
    completitud = models.TextField(db_column='Completitud', null=True, blank=True)
    datos_jefe = models.TextField(db_column='Datos_jefe', null=True, blank=True)
    antecedentes_jefe = models.TextField(db_column='Antecedentes_jefe', null=True, blank=True)
        
    class Meta:
        db_table = '[report].[V_Catatumbo_Individual]'
        managed = False  # Evita que Django intente modificar la tabla            
        
class CatatumboGrupo(models.Model):
    id = models.CharField(max_length=41, db_column='__id', primary_key=True)
    submission_date = models.TextField(db_column='SUBMISSIONDATE', null=True, blank=True)
    updated_at = models.TextField(db_column='UPDATEDAT', null=True, blank=True)
    fase = models.TextField(db_column='FASE', null=True, blank=True)
    submitter_id = models.TextField(db_column='SUBMITTERID', null=True, blank=True)
    submitter_name = models.TextField(db_column='SUBMITTERNAME', null=True, blank=True)
    attachments_present = models.TextField(db_column='ATTACHMENTSPRESENT', null=True, blank=True)
    attachments_expected = models.TextField(db_column='ATTACHMENTSEXPECTED', null=True, blank=True)
    status = models.TextField(db_column='STATUS', null=True, blank=True)
    review_state = models.TextField(db_column='REVIEWSTATE', null=True, blank=True)
    device_id = models.TextField(db_column='DEVICEID', null=True, blank=True)
    edits = models.TextField(db_column='EDITS', null=True, blank=True)
    form_version = models.TextField(db_column='FORMVERSION', null=True, blank=True)
    nota1 = models.TextField(db_column='NOTA1', null=True, blank=True)
    tiene_coca = models.TextField(db_column='TIENE COCA', null=True, blank=True)
    victima_posterior_2025 = models.TextField(db_column='VICTIMA POSTERIOR 2025', null=True, blank=True)
    nota15 = models.TextField(db_column='NOTA15', null=True, blank=True)
    tipo_linea_productiva = models.TextField(db_column='TIPO LINEA PRODUCTIVA', null=True, blank=True)
    condicion_linea_productiva = models.TextField(db_column='CONDICION LINEA PRODUCTIVA', null=True, blank=True)
    linea_productiva = models.TextField(db_column='LINEA PRODUCTIVA', null=True, blank=True)
    linea_productiva_fortalecimiento = models.TextField(db_column='LINEA PRODUCTIVA FORTALECIMIENTO', null=True, blank=True)
    linea_productiva_fortalecimiento_cual = models.TextField(db_column='LINEA PRODUCTIVA FORTALECIMIENTO CUAL', null=True, blank=True)
    experiencia_linea_productiva = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA', null=True, blank=True)
    experiencia_linea_productiva_anos = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS', null=True, blank=True)
    departamento = models.TextField(db_column='DEPARTAMENTO', null=True, blank=True)
    municipio = models.TextField(db_column='MUNICIPIO', null=True, blank=True)
    vereda = models.TextField(db_column='VEREDA', null=True, blank=True)
    condicion_linea_productiva_no_agropecuaria = models.TextField(db_column='CONDICION LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    linea_productiva_no_agropecuaria = models.TextField(db_column='LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    experiencia_linea_productiva_no_agropecuaria = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA NO AGROPECUARIA', null=True, blank=True)
    experiencia_linea_productiva_anos_no_agropecuaria = models.TextField(db_column='EXPERIENCIA LINEA PRODUCTIVA ANOS NO AGROPECUARIA', null=True, blank=True)
    cabecera_municipal = models.TextField(db_column='CABECERA MUNICIPAL', null=True, blank=True)
    fecha = models.TextField(db_column='FECHA', null=True, blank=True)
    grupo_productores = models.TextField(db_column='GRUPO PRUDUCTORES', null=True, blank=True)
    tipo_organizacion = models.TextField(db_column='TIPO ORGANIZACION', null=True, blank=True)
    tipo_organizacion_cual = models.TextField(db_column='TIPO ORGANIZACION CUAL', null=True, blank=True)
    identificacion_organizacion = models.TextField(db_column='IDENTIFICACION ORGANIZACION', null=True, blank=True)
    representante = models.TextField(db_column='REPRESENTANTE', null=True, blank=True)
    cedula_representante = models.TextField(db_column='CEDULA REPRESENTANTE', null=True, blank=True)
    telefono = models.TextField(db_column='TELEFONO', null=True, blank=True)
    correo = models.TextField(db_column='CORREO', null=True, blank=True)
    departamento_influencia = models.TextField(db_column='DEPARTAMENTO INFLUENCIA', null=True, blank=True)
    municipio_influencia = models.TextField(db_column='MUNICIPIO INFLUENCIA', null=True, blank=True)
    vereda_influencia = models.TextField(db_column='VEREDA INFLUENCIA', null=True, blank=True)
    fecha_creacion = models.TextField(db_column='FECHA CREACION', null=True, blank=True)
    principales_lineas_productivas = models.TextField(db_column='PRINCIPALES LINEAS PRODUCTIVAS', null=True, blank=True)
    principales_lineas_productivas_cual = models.TextField(db_column='PRINCIPALES LINEAS PRODUCTIVAS CUAL', null=True, blank=True)
    
    
    
    class Meta:
        db_table = '[stg].[Catatumbo_Grupo]'
        managed = False  # Evita que Django intente modificar la tabla    


class CatatumboNucleoAsociativo(models.Model):
    id_internal = models.CharField(max_length=255, db_column='__id', null=True, blank=True)
    tiene_coca = models.CharField(max_length=255, db_column='TIENE COCA', null=True, blank=True)
    identificacion = models.CharField(max_length=255, db_column='IDENTIFICACION', null=True, blank=True)
    validacion_identificacion_pnis = models.CharField(max_length=255, db_column='VALIDACION IDENTIFICACION PNIS', null=True, blank=True)
    identificacion_valida_pnis = models.CharField(max_length=255, db_column='IDENTIFICACION VALIDA PNIS', null=True, blank=True)
    validacion_identificacion_proveedores = models.CharField(max_length=255, db_column='VALIDACION IDENTIFICACION PROVEEDORES', null=True, blank=True)
    identificacion_valida_proveedores = models.CharField(max_length=255, db_column='IDENTIFICACION VALIDA PROVEEDORES', null=True, blank=True)
    validacion_identificacion_inscritos = models.CharField(max_length=255, db_column='VALIDACION IDENTIFICACION INSCRITOS', null=True, blank=True)
    identificacion_valida_inscritos = models.CharField(max_length=255, db_column='IDENTIFICACION VALIDA INSCRITOS', null=True, blank=True)
    codigo_familias_encuesta = models.CharField(max_length=255, db_column='CODIGO FAMILIAS ENCUESTA', null=True, blank=True)
    validacion_codigo_familias_encuesta = models.CharField(max_length=255, db_column='VALIDACION CODIGO FAMILIAS ENCUESTA', null=True, blank=True)
    codigo_familias_encuesta_valida1 = models.CharField(max_length=255, db_column='CODIGO FAMILIAS ENCUESTA VALIDA1', null=True, blank=True)
    codigo_familias_encuesta_valida = models.CharField(max_length=255, db_column='CODIGO FAMILIAS ENCUESTA VALIDA', null=True, blank=True)
    linea_productiva = models.CharField(max_length=255, db_column='LINEA PRODUCTIVA', null=True, blank=True)
    tipo_linea_productiva_1 = models.CharField(max_length=255, db_column='TIPO LINEA PRODUCTIVA_1', null=True, blank=True)
    condicion_linea_productiva = models.CharField(max_length=255, db_column='CONDICION LINEA PRODUCTIVA', null=True, blank=True)
    fecha = models.CharField(max_length=255, null=True, blank=True)
    tipo_linea_productiva = models.CharField(max_length=255, db_column='TIPO LINEA PRODUCTIVA', null=True, blank=True)
    nombres = models.CharField(max_length=255, db_column='NOMBRES', null=True, blank=True)
    apellidos = models.CharField(max_length=255, db_column='APELLIDOS', null=True, blank=True)
    tipo_documento = models.CharField(max_length=255, db_column='TIPO DOCUMENTO', null=True, blank=True)
    numero_documento = models.CharField(max_length=255, db_column='NUMERO DOCUMENTO', null=True, blank=True)
    documento_valido = models.CharField(max_length=255, db_column='DOCUMENTO VALIDO', null=True, blank=True)
    foto_documento_frente = models.CharField(max_length=255, db_column='FOTO DOCUMENTO FRENTE', null=True, blank=True)
    foto_documento_respaldo = models.CharField(max_length=255, db_column='FOTO DOCUMENTO RESPALDO', null=True, blank=True)
    fecha_nacimiento = models.CharField(max_length=255, db_column='FECHA NACIMIENTO', null=True, blank=True)
    edad = models.CharField(max_length=255, db_column='EDAD', null=True, blank=True)
    sexo = models.CharField(db_column='SEXO', max_length=255, null=True, blank=True)
    madre_cabeza_familia = models.CharField(max_length=255, db_column='MADRE CABEAZA FAMILIA', null=True, blank=True)
    orientacion = models.CharField(max_length=255, db_column='ORIENTACION', null=True, blank=True)
    telefono = models.CharField(max_length=255, db_column='TELEFONO', null=True, blank=True)
    correo = models.CharField(max_length=255, db_column='CORREO', null=True, blank=True)
    tipo_ciudadano = models.CharField(max_length=255, db_column='TIPO CIUDADANO', null=True, blank=True)
    pueblo = models.CharField(max_length=255, null=True, blank=True)
    etnico = models.CharField(max_length=255, null=True, blank=True)
    nombre_comunidad = models.CharField(max_length=255, db_column='NOMBRECOMUNIDAD', null=True, blank=True)
    censo = models.CharField(max_length=255, null=True, blank=True)
    nombre_comunidad1 = models.CharField(max_length=255, db_column='NOMBRECOMUNIDAD1', null=True, blank=True)
    lote_etnico = models.CharField(max_length=255, db_column='LOTEETNICO', null=True, blank=True)
    condicion = models.CharField(max_length=255, null=True, blank=True)
    discapacidad = models.CharField(max_length=255, null=True, blank=True)
    educacion = models.CharField(max_length=255, null=True, blank=True)
    numero_personas = models.CharField(max_length=255, db_column='NUMERO PERSONAS', null=True, blank=True)
    numero_documentos_personas_nucleo = models.CharField(max_length=255, db_column='NUMERO DOCUMENTOS PERSONAS NUCLEO', null=True, blank=True)
    nombres_documentos_personas_nucleo = models.CharField(max_length=255, db_column='NOMBRES DOCUMENTOS PERSONAS NUCLEO', null=True, blank=True)
    nota3 = models.CharField(max_length=255, null=True, blank=True)
    numero_total_predios_inscribir = models.CharField(max_length=255, db_column='NUMERO TOTAL PREDIOS INSCRIBIR', null=True, blank=True)
    numero_predios_inscribir = models.CharField(max_length=255, db_column='NUMERO PREDIOS INSCRIBIR', null=True, blank=True)
    
    class Meta:
        db_table = '[stg].[Catatumbo_Nucleo_Asociativo]'
        managed = False  # Evita que Django intente modificar la tabla    
