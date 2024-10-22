from django.shortcuts import render
from django.http import JsonResponse 
from bokitas.models import Tarea

 
# Create your views here.
def tareas(request):  
    all_events = Tarea.objects.all().order_by('start')
    context = {
        "events":all_events,
    }
    return render(request,'tareas.html',context)
 
def all_events(request):
    all_events = Tarea.objects.all().order_by('start')
    out = []
    for event in all_events:
        out.append({
            'title': event.title,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })                                                                                                   
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Tarea(title=str(title), start=start, end=end)
    event.save()
    data = {}

    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Tarea.objects.get(id=id)
    event.start = start
    event.end = end
    event.title = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Tarea.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)