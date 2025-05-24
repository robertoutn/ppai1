from django.shortcuts import render, get_object_or_404, redirect
from .models import OrdenInspeccion
from .forms import CierreOrdenInspeccionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def cerrar_orden_inspeccion(request, pk):
    orden = get_object_or_404(OrdenInspeccion, pk=pk)
    if request.method == 'POST':
        form = CierreOrdenInspeccionForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.save()
            messages.success(request, 'La orden de inspección fue cerrada correctamente.')
            return redirect('detalle_orden_inspeccion', pk=orden.pk)
    else:
        form = CierreOrdenInspeccionForm(instance=orden)
    return render(request, 'inspeccion/cerrar_orden_inspeccion.html', {'form': form, 'orden': orden})

@login_required
def detalle_orden_inspeccion(request, pk):
    orden = get_object_or_404(OrdenInspeccion, pk=pk)
    return render(request, 'inspeccion/detalle_orden_inspeccion.html', {'orden': orden})

@login_required
def lista_ordenes(request):
    ordenes = OrdenInspeccion.objects.all().order_by('-fecha_generacion')
    return render(request, 'inspeccion/lista_orden_inspeccion.html', {'ordenes': ordenes})
