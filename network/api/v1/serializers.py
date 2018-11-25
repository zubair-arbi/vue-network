from rest_framework import serializers

from network import models


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = ('id', 'address')


class SystemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.System
        fields = ('id', 'name')


class SystemSerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True, read_only=True)
    connected_systems = SystemListSerializer(many=True, read_only=True)

    class Meta:
        model = models.System
        fields = ('id', 'name', 'areas', 'connected_systems')
