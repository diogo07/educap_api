from rest_framework import serializers
from educap_api.models import Usuario
from django.contrib.auth.models import User

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        depth = 1

class UsuarioGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        depth = 1

class UsuarioCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'