from django.db import models

class Post(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=500)
    data = models.DateField()

    def __str__(self):
        return self.titulo

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    copyright = models.TextField(max_length=500)

    def __str__(self):
        return self.titulo
