from django.db import models

# Create your models here.
from Dispositivos.models import Dispositivo
from Solicitante.models import Solicitantes


class Orden(models.Model):
    numero=models.CharField(max_length=60,default="GADMED-UIT-2021")
    fecha=models.DateTimeField(auto_now_add=True)
    solicitante=models.ForeignKey(Solicitantes,on_delete=models.CASCADE)
    aprobado_por=models.CharField(max_length=60, null=True)
    tipo_de_dispositivo=models.ForeignKey(Dispositivo,on_delete=models.CASCADE)
    codigo_de_inventario=models.CharField(max_length=60,null=True,blank=True)
    descripcion_del_problema=models.TextField()
    detalles_del_equipo=models.TextField()
    receptor=models.CharField(max_length=60)
    autorizado=models.CharField(max_length=60)
    revisado_por=models.CharField(max_length=60)
    detalle_tecnico_del_problema=models.TextField()
    descripcion_de_la_solucion=models.TextField()
    materiales_utilizados=models.TextField()
    herramientas_utilizadas=models.TextField()
    tipos_de_servicio=models.TextField()
    entregado_por=models.CharField(max_length=60)
    estado=models.BooleanField(default=True)
    fecha_entrega=models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name_plural='Ordenes de Trabajo'