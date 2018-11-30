from rest_framework import serializers

from network.models import Area, System


class AreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'address')


class SystemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ('id', 'name')


class ConnectedSystemsSerializer(serializers.ModelSerializer):
    areas = AreaListSerializer(many=True, read_only=False)
    connected_systems = SystemListSerializer(many=True, read_only=False)

    class Meta:
        model = System
        fields = ('id', 'name', 'areas', 'connected_systems')


class AreaSerializer(serializers.ModelSerializer):
    connected_systems = ConnectedSystemsSerializer(source='system_set', many=True, read_only=True)

    class Meta:
        model = Area
        fields = ('id', 'address', 'connected_systems')

    def update(self, instance, validated_data):
        connected_systems_data = self.initial_data.pop('connected_systems')

        # now get extra optional parameters to unlink connected systems
        unlinked_connected_systems_data = self.initial_data.get('unlinked_connected_systems', [])

        # now try to extra optional parameters to link/unlink nested systems
        nested_systems_data = self.initial_data.get('nested_systems', [])
        unlinked_nested_systems_data = self.initial_data.get('unlinked_nested_systems', [])

        for connected_system in connected_systems_data:
            connected_system_object, __ = System.objects.get_or_create(name=connected_system['name'])
            connected_system_object.areas.add(instance)

        for connected_system in unlinked_connected_systems_data:
            connected_system_object = System.objects.filter(name=connected_system['name']).first()
            if connected_system_object:
                connected_system_object.areas.remove(instance)

        for nested_system in nested_systems_data:
            parent_system_object, __ = System.objects.get_or_create(name=nested_system['parent_system'])
            child_system_object, __ = System.objects.get_or_create(name=nested_system['name'])
            if parent_system_object != child_system_object:
                parent_system_object.connected_systems.add(child_system_object)

        for nested_system in unlinked_nested_systems_data:
            parent_system_object, __ = System.objects.get_or_create(name=nested_system['parent_system'])
            child_system_object, __ = System.objects.get_or_create(name=nested_system['name'])
            parent_system_object.connected_systems.remove(child_system_object)

        return instance


class SystemSerializer(serializers.ModelSerializer):
    areas = AreaListSerializer(many=True, read_only=False)
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
