from django.db import models

class Ativo(models.Model):
    ativo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    volume = models.IntegerField()
    setor = models.CharField(max_length=250)

    def __str__(self):
        return self.ativo
    
class AnalisadorAtivo(models.Model):
    ativo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    volume = models.IntegerField()
    dh_consullta = models.DateTimeField()
    preco = models.FloatField()

    def __str__(self):
        return self.ativo