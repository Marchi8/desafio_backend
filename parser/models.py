from django.db import models
import uuid

# Create your models here.
class Type(models.TextChoices):
    Débito = "1"
    Boleto = "2"
    Financiamento = "3"
    Crédito = "4"
    Recebimento_Empréstimo = "5"
    Vendas = "6"
    Recebimento_TED = "7"
    Recebimento_DOC = "8"
    Aluguel = "9"


class DocFile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.CharField(max_length=1, choices=Type.choices)
    data = models.DateField()
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono_loja = models.CharField(max_length=16)
    nome_loja = models.CharField(max_length=22)
