from django.shortcuts import render
from .models import Artigo

# Create your views here.
def inicio(request):
    artigos = Artigo.objects.all()
    return render(request, 'inicio.html', {'artigos': artigos})