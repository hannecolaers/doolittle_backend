from rest_framework import serializers, status
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.exceptions import APIException
from floorplan.models import Room, Space


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'type', 'color')

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, room, validated_data):
        room.name = validated_data.get('name', room.name)
        room.type = validated_data.get('type', room.type)
        room.color = validated_data.get('color', room.color)
        room.save()
        return room


class SpaceSerializer(serializers.HyperlinkedModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Space
        fields = ('x', 'y', 'employee_id', 'room')
        unique_together = (("x", "y"),)
        validators = [
            UniqueTogetherValidator(
                queryset = Space.objects.all(),
                fields = ('x', 'y')
            )
        ]

    def create(self, validated_data):
        room_data = validated_data.pop('room')
        if Room.objects.filter(name=room_data["name"]).exists():
            room = Room.objects.get(name=room_data["name"])
            validated_data.update({'room': room})
            space = Space.objects.create(**validated_data)
            return space
        else:
            raise InvalidRoomError()

    def update(self, space, validated_data):
        space.x = validated_data.get('x', space.x)
        space.y = validated_data.get('y', space.y)
        space.employee_id = validated_data.get('employee_id', space.employee_id)
        if validated_data.get('room'):
            room_name = validated_data.get('room').get('name')
            if Room.objects.filter(name=room_name).exists():
                room = Room.objects.get(name=room_name)
                space.room = room
            else:
                raise InvalidRoomError()
        space.save()
        return space


class InvalidRoomError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Room does not exist"
