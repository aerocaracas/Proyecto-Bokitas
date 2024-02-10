from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bokitas.models import Centro

# Create your views here.
@login_required      
def proyecto(request):
    centro = Centro.objects.all()
    return render(request, 'proyecto.html',{
        'centro': centro
    })
