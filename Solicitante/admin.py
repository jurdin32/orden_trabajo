from django.contrib import admin

# Register your models here.
from Solicitante.models import Solicitantes
from orden_trabajo.snippers import Attr


@admin.register(Solicitantes)
class modelo(admin.ModelAdmin):
    list_display_links  = Attr(Solicitantes)
    list_display = Attr(Solicitantes)
