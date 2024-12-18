from django.shortcuts import render
from .models import Galeria
from django.core.paginator import Paginator

# Create your views here.

def galeria(request):
    galerias=Galeria.objects.all()
    paginator=Paginator(galerias, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/galeria.html', {"page_obj": page_obj})
    
    


