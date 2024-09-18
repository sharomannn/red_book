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
    order = Order(read_only=True)
    family = Family(read_only=True)
    sectors = Sector(many=True, read_only=True)

    order_id = serializers.IntegerField(required=False, allow_null=True)
    family_id = serializers.IntegerField(required=False, allow_null=True)
    sector_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)

    class Meta:
        model = models.RedBookEntry
        fields = '__all__'

    def create(self, validated_data: dict) -> models.RedBookEntry:
        sectors_id = validated_data.pop('incident_kind_ids', [])
        red_book_entry = super().create(validated_data)
        if sectors_id:
            red_book_entry.sectors.set(sectors_id)
        return red_book_entry

    def update(self, instance: models.RedBookEntry, validated_data: dict) -> models.RedBookEntry:
        sectors_id = validated_data.pop('sectors_id', [])
        instance = super().update(instance, validated_data)
        if sectors_id:
            instance.sectors.set(sectors_id)
        return instance


class Observation(serializers.ModelSerializer):
    class Meta:
        model = models.Observation
        fields = '__all__'
