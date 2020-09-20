from rest_framework import serializers
from educap_api.models import Curso

class CursoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        depth = 1

class CursoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        depth = 1

class CursoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'

    def create(self, validated_data):
        instance = Curso.objects.create(**validated_data)
        instance.save()

        return instance

class CursoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'