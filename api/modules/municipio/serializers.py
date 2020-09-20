from rest_framework import serializers
from educap_api.models import Municipio

class MunicipioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'
        depth = 1

class MunicipioGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'
        depth = 1

class MunicipioCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = '__all__'

    def create(self, validated_data):
        instance = Municipio.objects.create(**validated_data)
        instance.save()

        return instance

class MunicipioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'