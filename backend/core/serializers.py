from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core import models


class User(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = models.User
        fields = '__all__'

    def create(self, validated_data: dict) -> models.User:
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance: models.User, validated_data: dict) -> models.User:
        if validated_data.get('password'):
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)


class AuthorizeRequest(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthorizeResponse(serializers.Serializer):
    is_valid = serializers.BooleanField()
    msg = serializers.CharField(required=False)
    token = serializers.CharField(required=False)
    user = User(required=False)


class Family(serializers.ModelSerializer):
    class Meta:
        model = models.Family
        fields = '__all__'


class Order(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class Sector(serializers.ModelSerializer):
    class Meta:
        model = models.Sector
        fields = '__all__'


class RedBookEntry(serializers.ModelSerializer):
    order = Order()
    family = Family()
    sectors = Sector(many=True)

    class Meta:
        model = models.RedBookEntry
        fields = '__all__'
