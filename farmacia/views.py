from django.shortcuts import render
from .models import Post

# Create your views here.
def inicio(request):
    meu_post = Post.objects.get(id = 1)
    return render(request, 'inicio.html'), {'post1': meu_post}