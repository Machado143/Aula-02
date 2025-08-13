from django.db import models

# Create your models here.
class Artigo(models.Model):
    """Artigo sobre medicamentos e farmácia"""
    
    autor = models.CharField(max_length=32)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'  # usa a mesma tabela do banco
        ordering = ['-data_postagem']
        
    def __str__(self):
        return f"{self.titulo} - {self.autor}"