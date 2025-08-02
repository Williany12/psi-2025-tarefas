from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Autores"


class Post(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=500)
    data = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Postagens"

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    copyright = models.TextField(max_length=500)

    def __str__(self):
        return self.titulo
    
