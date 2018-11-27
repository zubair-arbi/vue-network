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

        # now get extra optional parameters to unlink areas and connected systems
        unlinked_areas_data = self.initial_data.get('unlinked_areas', [])
        unlinked_connected_systems_data = self.initial_data.get('unlinked_connected_systems', [])

        instance = super(SystemSerializer, self).update(instance, validated_data)
        for area in areas_data:
            area_object, __ = Area.objects.get_or_create(address=area['address'])
            instance.areas.add(area_object)

        for connected_system in connected_systems_data:
            connected_system_object, __ = System.objects.get_or_create(name=connected_system['name'])
            # Avoid accidental circular linking with same system
            if instance.name != connected_system_object.name:
                instance.connected_systems.add(connected_system_object)

        for area in unlinked_areas_data:
            area_object = Area.objects.filter(address=area['address']).first()
            if area_object:
                instance.areas.remove(area_object)

        for connected_system in unlinked_connected_systems_data:
            connected_system_object = System.objects.filter(name=connected_system['name']).first()
            if connected_system_object:
                instance.connected_systems.remove(connected_system_object)

        return instance
