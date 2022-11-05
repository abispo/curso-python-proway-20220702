from django.db import models
from slugify import slugify


class Mensagem(models.Model):

    titulo = models.CharField(max_length=200, null=False)
    corpo = models.TextField()
    autor = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return self.__str__

    def slug_titulo(self):
        return slugify(self.titulo)
