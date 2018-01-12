from rest_framework import serializers, status
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.exceptions import APIException
from floorplan.models import Room, Space


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, room, validated_data):
        room.name = validated_data.get('name', room.name)
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
                queryset=Space.objects.all(),
                fields=('x', 'y')
            )
        ]

    def create(self, validated_data):
        room_data = validated_data.pop('room')
        if Room.objects.filter(name=room_data["name"]).exists():
            Room.objects.get(**room_data)
            room = Room.objects.get(name=room_data["name"])
            validated_data.update({'room': room})
            space = Space.objects.create(**validated_data)
            space.room = room
            return space
        else:
            raise InvalidRoomError()

    def update(self, space, validated_data):
        space.x = validated_data.get('x', space.x)
        space.y = validated_data.get('y', space.y)
        space.employee_id = validated_data.get('employee_id', space.employee_id)
        if validated_data.get('room'):
            room_name = validated_data.get('room').get('name')
            room = Room.objects.get(name=room_name)
            space.room = room
            space.save()
        return space


class InvalidRoomError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Room does not exist"


def printLog(*args, **kwargs):
    print(*args, **kwargs)
    with open('output.out', 'a') as file:
        print(*args, **kwargs, file=file)
