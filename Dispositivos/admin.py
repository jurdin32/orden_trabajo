from django.contrib import admin

# Register your models here.
from Dispositivos.models import Dispositivo
from orden_trabajo.snippers import Attr

@admin.register(Dispositivo)
class modelo(admin.ModelAdmin):
    list_display_links  = Attr(Dispositivo)
    list_display = Attr(Dispositivo)
