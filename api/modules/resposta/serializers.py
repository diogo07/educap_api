from rest_framework import serializers
from educap_api.models import Resposta

class RespostaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'
        depth = 1

class RespostaGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'
        depth = 1

class RespostaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resposta
        fields = '__all__'

    def create(self, validated_data):
        instance = Resposta.objects.create(**validated_data)
        instance.save()

        return instance

class RespostaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'