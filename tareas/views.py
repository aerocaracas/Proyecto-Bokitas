from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from tareas.forms import TareaForm
from bokitas.models import Tarea
from django.utils import timezone
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required  
def tareas(request):
    
    if request.method == 'GET':
        fecha = date.today()
        form = TareaForm
        tareas = Tarea.objects.filter(user=request.user, completado__isnull=True)
        tareas_mes = Tarea.objects.filter(fecha_inicio__year=fecha.year, fecha_inicio__month=fecha.month, user=request.user,completado__isnull=True)
        event_list = []
        
        for event in tareas:
            event_list.append(
                {   "id": event.id,
                    "title": event.titulo,
                    "start": event.fecha_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.fecha_fin.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": event.descripcion,
                }
            )
        
        context = {"form": form, "events": tareas,
                   "events_month": tareas_mes}
        return render(request, 'tareas.html', context)

    else:
        try:
            form = TareaForm(request.POST)
            new_tarea = form.save(commit=False)
            new_tarea.user = request.user
            new_tarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea_crear.html', {
            'form': TareaForm,
            'error': 'Datos incorectos, Favor verificar la información'
            })




'''

class CalendarViewNew():
    login_url = "accounts:signin"
    template_name = "calendarapp/calendar.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events(user=request.user)
        events_month = Event.objects.get_running_events(user=request.user)
        event_list = []
        # start: '2020-09-16T16:00:00'
        for event in events:
            event_list.append(
                {   "id": event.id,
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": event.description,
                }
            )
        
        context = {"form": forms, "events": event_list,
                   "events_month": events_month}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("calendarapp:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


'''


@login_required  
def tarea_crear(request):
    if request.method == 'GET':
        return render(request, 'tarea_crear.html', {
            'form': TareaForm
        })
    else:
        try:
            form = TareaForm(request.POST)
            new_tarea = form.save(commit=False)
            new_tarea.user = request.user
            new_tarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea_crear.html', {
            'form': TareaForm,
            'error': 'Datos incorectos, Favor verificar la información'
            })

@login_required      
def tarea_detalle(request, tarea_id):
    if request.method == 'GET':
        tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
        form = TareaForm(instance=tareas)
        return render(request, 'tarea_detalle.html',{
            'tareas':tareas,
            'form': form
        })
    else:
        try:
            tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
            form = TareaForm(request.POST, instance=tareas)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea_detalle.html',{
            'tareas':tareas,
            'form': form,
            'error': "Error al actualizar la Tarea"
        })

@login_required  
def tarea_completada(request):
    tareas = Tarea.objects.filter(user=request.user, completado__isnull=False).order_by('-completado')
    return render(request, 'tarea_completada.html', {
        'tareas': tareas
    })

@login_required  
def tarea_complatar(request, tarea_id):
    tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tareas.completado = timezone.now()
        tareas.save()
        return redirect('tareas')

@login_required  
def tarea_eliminar(request, tarea_id):
    tareas = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tareas.delete()
        return redirect('tareas')

