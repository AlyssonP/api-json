from django.db import models

# Create your models here.

class Filme(models.Model):
    ano_lancamento = models.IntegerField() 
    titulo = models.CharField(max_length=200) 
    direcao = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    empresa_produtora_br_majoritaria = models.CharField(max_length=200)
    uf = models.CharField(max_length=100)
    distribuidora = models.CharField(max_length=100)
    renda = models.IntegerField()

    def __str__(self):
        return self.titulo

class SalasUF(models.Model):
    uf = models.CharField(max_length=2)
    qtd_salas = models.IntegerField()
    ano_atualizacao = models.IntegerField()

    def __str__(self):
        return str(self.uf)+", "+str(self.qtd_salas)