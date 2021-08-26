from django.db import models


# Create your models here.
class Solicitantes(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=60)
    cargo = models.CharField(max_length=60)
    unidad = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural='Datos del Solicitante'

    def __str__(self):
        return self.nombre