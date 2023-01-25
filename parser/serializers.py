from rest_framework import serializers
from .models import DocFile
import ipdb


class ParseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocFile
        fields = [
            "id",
            "tipo",
            "data",
            "valor",
            "cpf",
            "cartao",
            "hora",
            "dono_loja",
            "nome_loja",
        ]
        read_only_fields = [
            "id",
            "tipo",
            "data",
            "valor",
            "cpf",
            "cartao",
            "hora",
            "dono_loja",
            "nome_loja",
        ]

    def create(self, validated_data):
        ipdb.set_trace()
        return DocFile.objects.create(**validated_data)
