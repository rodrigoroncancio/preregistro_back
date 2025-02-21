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