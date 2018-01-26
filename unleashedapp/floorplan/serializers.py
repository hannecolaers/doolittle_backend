from rest_framework import serializers, status
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.exceptions import APIException
from floorplan.models import Room, Space


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, room, validated_data):
        room.name = validated_data.get('name', room.name)
        room.type = validated_data.get('type', room.type)
        room.color = validated_data.get('color', room.color)
        room.save()
        return room


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = '__all__'
        unique_together = (("x", "y"),)
        validators = [
            UniqueTogetherValidator(
                queryset=Space.objects.all(),
                fields=('x', 'y')
            )
        ]

    def create(self, validated_data):
        space = Space.objects.create(**validated_data)
        return space

    def update(self, space, validated_data):
        space.x = validated_data.get('x', space.x)
        space.y = validated_data.get('y', space.y)
        space.employee = validated_data.get('employee', space.employee)
        space.room = validated_data.get('room', space.room)
        space.save()
        return space

