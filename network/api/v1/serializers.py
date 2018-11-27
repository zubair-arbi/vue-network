from rest_framework import serializers

from network.models import Area, System


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'address')


class SystemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ('id', 'name')


class SystemSerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True, read_only=False)
    connected_systems = SystemListSerializer(many=True, read_only=False)

    class Meta:
        model = System
        fields = ('id', 'name', 'areas', 'connected_systems')

    def update(self, instance, validated_data):
        areas_data = validated_data.pop('areas')
        connected_systems_data = validated_data.pop('connected_systems')
        instance = super(SystemSerializer, self).update(instance, validated_data)

        for area in areas_data:
            area_object, __ = Area.objects.get_or_create(address=area['address'])
            instance.areas.add(area_object)

        for connected_system in connected_systems_data:
            connected_system_object, __ = System.objects.get_or_create(name=connected_system['name'])
            if instance.name != connected_system_object.name:
                instance.connected_systems.add(connected_system_object)

        return instance
