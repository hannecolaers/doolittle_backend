from rest_framework import serializers
from floorplan.models import Room, Space


class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = ('url', 'id', 'name')

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Room` instance, given the validated data.
        """
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Room` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class SpaceSerializer(serializers.Serializer):
    class Meta:
        model = Space
        fields = ('url', 'x', 'y', 'employee_id', 'room_id')

    x = serializers.IntegerField(label='x')
    y = serializers.IntegerField(label='y')
    employee_id = serializers.IntegerField(label='employee_id')
    room_id = serializers.IntegerField(label='room_id')

    def create(self, validated_data):
        """
        Create and return a new `Space` instance, given the validated data.
        """
        return Space.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Space` instance, given the validated data.
        """
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.room_id = validated_data.get('room_id', instance.room_id)
        instance.save()
        return instance
