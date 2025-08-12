from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Esta é a classe que representa um post do blog.
    vai possuir relação com :model:`auth.User`

    """

    autor = models.CharField(max_length=32) #campo texto
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'posts'  # nome da tabela no banco de dados