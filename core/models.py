from django.db import models
from django.contrib.auth import get_user_model

class Staff(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s" % self.user.first_name + " " + self.user.last_name

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
    # email = models.EmailField(max_length=255, null=True, blank=True, db_column='Email')
    civilstatusid = models.ForeignKey('CivilStatus', on_delete=models.SET_NULL, null=True, blank=True, db_column='CivilStatusId')
    # headofhousehold = models.BooleanField(default=False, db_column='HeadOfHousehold')
    # motherheadoffamily = models.BooleanField(default=False, db_column='MotherHeadOfFamily')
    conditionid = models.ForeignKey('Condition', on_delete=models.SET_NULL, null=True, blank=True, db_column='ConditionId')
    occupationid = models.ForeignKey('Occupation', on_delete=models.SET_NULL, null=True, blank=True, db_column='OccupationId')
    educationid = models.ForeignKey('Education', on_delete=models.SET_NULL, null=True, blank=True, db_column='EducationId')
    healthaffiliationtypeid = models.ForeignKey('HealthAffiliationType', on_delete=models.SET_NULL, null=True, blank=True, db_column='HealthAffiliationTypeId')
    subjectofspecialprotectionid = models.ForeignKey('Subjectofspecialprotection', on_delete=models.SET_NULL, null=True, blank=True, db_column='SubjectOfSpecialProtectionId')
    # etniaid = models.IntegerField(null=True, blank=True, db_column='EtniaId')
    # communitylocation = models.CharField(max_length=255, null=True, blank=True, db_column='CommunityLocation')
    # communityname = models.CharField(max_length=255, null=True, blank=True, db_column='CommunityName')
    # etnianame = models.CharField(max_length=255, null=True, blank=True, db_column='EtniaName')
    # registryofyourethniccommunity = models.BooleanField(default=False, db_column='RegistryOfYourEthnicCommunity')
    # productiveprojectislocatedethnicterritory = models.BooleanField(default=False, db_column='ProductiveProjectIsLocatedEthnicTerritory')
    # monthlyincome = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='MonthlyIncome')
    # monthlyexpenses = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='MonthlyExpenses')
    # department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True, db_column='DepartmentId')
    # municipality = models.ForeignKey('Municipality', on_delete=models.SET_NULL, null=True, blank=True, db_column='MunicipalityId')
    # township = models.ForeignKey('Township', on_delete=models.SET_NULL, null=True, blank=True, db_column='TownshipId')
    # propertynamehome = models.CharField(max_length=255, null=True, blank=True, db_column='PropertyNameHome')
    # areahome = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, db_column='AreaHome')
    # landcoordinates = models.TextField(null=True, blank=True, db_column='LandCoordinates')
    # permanence = models.CharField(max_length=255, null=True, blank=True, db_column='Permanence')
    # acquisitionhome = models.ForeignKey('Acquisitionfarm', on_delete=models.SET_NULL, null=True, blank=True, db_column='AcquisitionHomeId')
    # documentacquisitionhome = models.CharField(max_length=255, null=True, blank=True, db_column='DocumentAcquisitionHome')
    # dependents = models.PositiveIntegerField(null=True, blank=True, db_column='Dependents')
    # minorsinfamily = models.PositiveIntegerField(null=True, blank=True, db_column='MinorsInFamily')
    # acquisitionhomeidentificationtypeid = models.IntegerField(null=True, blank=True, db_column='AcquisitionHomeIdentificationTypeId')
    # acquisitionhomeidentificationnumber = models.CharField(max_length=50, null=True, blank=True, db_column='AcquisitionHomeIdentificationNumber')
    # landownership = models.CharField(max_length=255, null=True, blank=True, db_column='LandOwnership')
    # departmentfarmid = models.IntegerField(null=True, blank=True, db_column='DepartmentFarmId')
    # municipalityfarmid = models.IntegerField(null=True, blank=True, db_column='MunicipalityFarmId')
    # townshipfarmid = models.IntegerField(null=True, blank=True, db_column='TownshipFarmId')
    # villagefarmid = models.IntegerField(null=True, blank=True, db_column='VillageFarmId')
    # acquisitionfarmid = models.IntegerField(null=True, blank=True, db_column='AcquisitionFarmId')
    # propertynamefarm = models.CharField(max_length=255, null=True, blank=True, db_column='PropertyNameFarm')
    # areafarm = models.FloatField(null=True, blank=True, db_column='AreaFarm')
    # landcoordinates2 = models.CharField(max_length=255, null=True, blank=True, db_column='LandCoordinates2')
    # documentacquisitionfarm = models.CharField(max_length=255, null=True, blank=True, db_column='DocumentAcquisitionFarm')
    # acquisitionfarmidentificationtypeid = models.IntegerField(null=True, blank=True, db_column='AcquisitionFarmIdentificationTypeId')
    # acquisitionfarmidentificationnumber = models.CharField(max_length=50, null=True, blank=True, db_column='AcquisitionFarmIdentificationNumber')
    # rootedtomunicipality = models.BooleanField(default=False, db_column='RootedToMunicipality')
    # landrelationshiptype = models.CharField(max_length=255, null=True, blank=True, db_column='LandRelationshipType')
    # landdocumenttype = models.CharField(max_length=255, null=True, blank=True, db_column='LandDocumentType')
    # landownername = models.CharField(max_length=255, null=True, blank=True, db_column='LandOwnerName')
    # residentsonland = models.PositiveIntegerField(null=True, blank=True, db_column='ResidentsOnLand')
    # haslegalactivities = models.BooleanField(default=False, db_column='HasLegalActivities')
    # LegalActivitiesid = models.IntegerField(null=True, blank=True, db_column='LegalActivitiesId')
    # familyexclusiveusage = models.BooleanField(default=False, db_column='FamilyExclusiveUsage')
    # familyotherlands = models.BooleanField(default=False, db_column='FamilyOtherLands')
    # productiveline = models.ForeignKey('ProductiveLine', on_delete=models.SET_NULL, null=True, blank=True, db_column='ProductiveLineId')
    # establishment = models.CharField(max_length=255, null=True, blank=True, db_column='Establishment')
    # strengthening = models.CharField(max_length=255, null=True, blank=True, db_column='Strengthening')
    # signature = models.TextField(null=True, blank=True, db_column='Signature')
    # reservation_name = models.CharField(max_length=255, null=True, blank=True, db_column='ReservationName')
    # accreditation_document_pdf = models.FileField(upload_to='documents/', null=True, blank=True, db_column='AccreditationDocumentPdf')
    # economicactivity = models.CharField(max_length=255, null=True, blank=True, db_column='EconomicActivity')
    # experienceproductionline = models.CharField(max_length=255, null=True, blank=True, db_column='ExperienceProductionLine')
    # yearsexperienceproductionline = models.IntegerField(null=True, blank=True, db_column='YearsExperienceProductionLine')
    class Meta:
        db_table = 'Users'  # Asegura que el modelo apunte a la tabla existente en SQL Server
        managed = False  # Evita que Django intente modificar la tabla


