from django.contrib import admin

# Register your models here.
from Ordenes.models import Orden
from orden_trabajo.snippers import Attr


@admin.register(Orden)
class modelo(admin.ModelAdmin):
    list_display_links  = Attr(Orden)
    list_display = Attr(Orden)
