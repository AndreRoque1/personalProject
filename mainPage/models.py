from django.db import models

class utilizadores(models.Model):
    nome=models.CharField(max_length=100)
    nickname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    def __str__(self):
        return self.nome
