from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from bokitas.models import Beneficiario, Menor
from django.core.paginator import Paginator
from django.db.models import Q



# Sesion Menores.
@login_required  
def menores(request):

    menores = Menor.objects.all()
    query = ""
    page = request.GET.get('page',1)

    try:
        if "search" in request.POST:
            query = request.POST.get("searchquery")
            menores = Menor.objects.filter(Q(cedula__icontains=query) | Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(cedula_bef__cedula__contains=query))
        paginator = Paginator(menores, 15)
        menores = paginator.page(page)
    except:
        raise Http404
    
    return render(request, 'menores.html',{
        'entity': menores,
        'query': query,
        'paginator': paginator
    })

