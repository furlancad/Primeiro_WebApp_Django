from django.db import models
import datetime

class Produto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Vendedor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Vendas(models.Model):
    nome_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nome_produto.nome