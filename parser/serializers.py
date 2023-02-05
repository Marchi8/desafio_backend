from rest_framework import serializers
from .models import DocFile
import ipdb


class ParseSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = DocFile
        fields = ["file"]

    def create(self, validated_data):

        # for key, value in validated_data.items():
        #     ipdb.set_trace()

        return DocFile.objects.create(**validated_data)
