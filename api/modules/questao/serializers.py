from rest_framework import serializers
from educap_api.models import Questao

class QuestaoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = '__all__'
        depth = 1

class QuestaoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = '__all__'
        depth = 1

class QuestaoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questao
        fields = '__all__'

    def create(self, validated_data):
        instance = Questao.objects.create(**validated_data)
        instance.save()

        return instance

class QuestaoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = '__all__'