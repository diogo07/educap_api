from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

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

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        m2m_fields = []
        for attr, value in validated_data.items():

            if attr == "password":
                instance.set_password(value)
            elif attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance