from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Artigo

# Register your models here.
@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_postagem']
    search_fields = ['titulo', 'autor']