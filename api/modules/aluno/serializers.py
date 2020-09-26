from rest_framework import serializers
from educap_api.models import Aluno

class AlunoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        depth = 1

class AlunoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        depth = 1

class AlunoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = '__all__'

    def create(self, validated_data):
        instance = Aluno.objects.create(**validated_data)
        instance.save()

        return instance

class AlunoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class AlunoCountByUniversidadeAndAnoSerializer(serializers.Serializer):
   enade_ano = serializers.IntegerField()
   total = serializers.IntegerField()