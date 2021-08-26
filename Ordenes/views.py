import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from simple_search import search_filter

from Dispositivos.models import Dispositivo
from Ordenes.models import Orden
from Solicitante.models import Solicitantes
from django.db.models import Q

from orden_trabajo.snippers import render_to_pdf


def index(request):
    documentos=""
    if request.GET.get('q'):
        search=request.GET.get('q')
        search_fields = ['solicitante__nombre', 'tipo_de_dispositivo__tipo_equipo', 'descripcion_del_problema','detalles_del_equipo']
        f = search_filter(search_fields, search)
        documentos = Orden.objects.filter(f)
    contexto={
        'solicitantes':Solicitantes.objects.all(),
        'dispositivos':Dispositivo.objects.all(),
        'documentos':documentos.order_by('fecha'),
    }
    return render(request,'index.html',contexto)


def registrar_solicitud(request):
    if request.POST:
        try:
            cantidad=Orden.objects.count()
            orden=Orden.objects.create(solicitante_id=request.POST.get('solicitante'),
                                       aprobado_por= request.POST.get('aprobado_por'),
                                       tipo_de_dispositivo_id=request.POST.get('tipo_dispositivo'),
                                       codigo_de_inventario=request.POST.get('codigo'),
                                       descripcion_del_problema=request.POST.get('descripcion_del_problema'),
                                       estado=False,
                                       )
            orden.numero ='GADMED-UIT-2021-%s'%(str.zfill(str(cantidad),7))
            orden.save()
            messages.add_message(request,messages.SUCCESS,"Registro Creado exitosamente..!")
        except:
            messages.add_message(request, messages.ERROR, "No se registro debido a que es necesario seleccionar el requiriente y el tipo de dispositivo o servicio..!")
            pass
    return HttpResponseRedirect("/")

def ver_ordenes(request, slug):
    orden=Orden.objects.get(numero=slug)
    if request.POST:
        orden.receptor=request.POST.get('recibido')
        orden.autorizado=request.POST.get('autorizado')
        orden.revisado_por=request.POST.get('revisado')
        orden.detalle_tecnico_del_problema=request.POST.get('problema')
        orden.descripcion_de_la_solucion=request.POST.get('solucion')
        orden.materiales_utilizados=request.POST.get('materiales')
        orden.herramientas_utilizadas=request.POST.get('herramientas')
        orden.tipos_de_servicio=request.POST.get('tipo_servicio')
        orden.detalles_del_equipo=request.POST.get('detalles_del_equipo')
        orden.estado=True
        orden.entregado_por=request.POST.get('entregado')
        orden.fecha_entrega=datetime.datetime.now()
        orden.save()
        messages.add_message(request, messages.SUCCESS, "Registro Creado exitosamente..!")
    contexto={
        'orden':orden,
    }
    return render(request,'ver_orden.html',contexto)

def reporte(request,slug):
    orden = Orden.objects.get(numero=slug)
    contexto={
        'orden':orden
    }
    return render_to_pdf('reporte.html',contexto)

def reporte_2(request,slug):
    orden = Orden.objects.get(numero=slug)
    contexto={
        'orden':orden
    }
    return render_to_pdf('reporte_2.html',contexto)