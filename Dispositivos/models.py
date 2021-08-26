from django.db import models

# Create your models here.

class Dispositivo(models.Model):
    tipo_equipo=models.CharField(max_length=60)

    class Meta:
        verbose_name_plural="Tipo de dispositivo"

    def __str__(self):
        return self.tipo_equipo