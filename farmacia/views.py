from django.shortcuts import render
from .models import Post

# Create your views here.
def inicio(request):
    meu_posts = Post.objects.all()
    return render(request, 'inicio.html', {'hahahahah': meu_posts})