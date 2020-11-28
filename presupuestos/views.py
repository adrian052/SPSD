from partidas.forms import PartidaForm
from presupuestos.forms import ActividadForm, PresupuestoForm
from django.shortcuts import redirect, render
from presupuestos.models import Presupuesto, Actividad

# Create your views here.

#Vista presupuestos
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'lista_presupuestos.html',{'presupuestos':presupuestos})

def nuevo_presupuesto(request):
    form =PresupuestoForm
    if request.method =='POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presupuestos:lista')
    else:
        form = PresupuestoForm()
    return render(request, 'nuevo_presupuesto.html',{'form':form})


def eliminar_presupuesto(request,anio):
    presupuesto = Presupuesto.objects.get(anio=anio)
    presupuesto.delete()
    return redirect('presupuestos:lista') 


def editar_presupuesto(request,anio):
    presupuesto =Presupuesto.objects.get(anio=anio)
    if request.method== 'POST':
        form= PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            form.save()
            return redirect('presupuestos:lista')
    else:
        form= PresupuestoForm(instance=presupuesto)
    return render(request, 'editar_presupuesto.html',{'form':form})
        

#Vista actividades


def lista_actividades(request):
    actividades= Actividad.objects.all()
    return render(request, 'lista_actividades.html',{'actividades':actividades})

def nueva_actividad(request):
    form = ActividadForm
    if request.method =='POST':
        form= ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividades:lista')
    else:
        form = ActividadForm()
    return render(request,'nueva_actividad.html',{'form':form})

def eliminar_actividad(request,id):
    actividad= Actividad.objects.get(id=id)
    actividad.delete()
    return redirect('actividades:lista')

def editar_actividad(request,id):
    actividad = Actividad.objects.get(id=id)
    if request.method== 'POST':
        form= ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividades:lista')
    else:
        form= ActividadForm(instance=actividad)
    return render(request, 'editar_actividad.html',{'form':form})
        