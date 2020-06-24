from django.db import models

class Voluntario(models.Model):
    Nome = models.CharField(max_length=200)
    Nascimento = models.CharField(max_length=200)
    Genero = models.CharField(max_length=200)
    Idade = models.CharField(max_length=2)
    Contato = models.CharField(max_length=600)
    ONG = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome
class Cachorro(models.Model):
    Nome = models.CharField(max_length=200)
    Raca = models.CharField(max_length=200)
    Genero = models.CharField(max_length=200)
    Cor = models.CharField(max_length=200)
    Idade = models.CharField(max_length=2)
    Vacinacao = models.CharField(max_length=3)
    Observacoes = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.Nome


class Gato(models.Model):
    Nome = models.CharField(max_length=200)
    Raca = models.CharField(max_length=200)
    Genero = models.CharField(max_length=200)
    Cor = models.CharField(max_length=200)
    Idade = models.CharField(max_length=2)
    Vacinacao = models.CharField(max_length=3)
    Observacoes = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.Nome


class petPerdido(models.Model):
    Nome = models.CharField(max_length=200)
    Contato = models.CharField(max_length=600)
    Dono = models.CharField(max_length=400, null=True)
    Raca = models.CharField(max_length=200)
    Genero = models.CharField(max_length=200)
    Cor = models.CharField(max_length=200)
    Idade = models.CharField(max_length=2)
    Data = models.CharField(max_length=200)
    Local = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome

class petAchado(models.Model):
    Nome = models.CharField(max_length=200)
    Raca = models.CharField(max_length=200)
    Genero = models.CharField(max_length=200)
    # Cor = models.CharField(max_length=200)
    Data = models.CharField(max_length=200)
    Local = models.CharField(max_length=200)
    Observacoes = models.CharField(max_length=400, null=True)
    Contato = models.CharField(max_length=600)
    Voluntario = models.ForeignKey(Voluntario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Raca
class petEncontrado(models.Model):
    Nome = models.ForeignKey(petPerdido, on_delete=models.SET_NULL, null=True)
    Dono = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Nome)

