from django.db import models
import uuid

# Create your models here.
class DocFile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.CharField(max_length=1)
    data = models.DateField()
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono_loja = models.CharField(max_length=16)
    nome_loja = models.CharField(max_length=22)
