from django.db import models

class Utilizadores(models.Model):
    nome = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    # META CLASS
    class Meta:
        verbose_name = 'Utilizadores'
        verbose_name_plural = 'Utilizadores'

    def __str__(self):
        return self.nome
