from rest_framework import serializers
from educap_api.models import Universidade

class UniversidadeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidade
        fields = '__all__'
        depth = 1

class UniversidadeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidade
        fields = '__all__'
        depth = 1

class UniversidadeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Universidade
        fields = '__all__'

    def create(self, validated_data):
        instance = Universidade.objects.create(**validated_data)
        instance.save()

        return instance

class UniversidadeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidade
        fields = '__all__'