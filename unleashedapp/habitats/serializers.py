from rest_framework import serializers
from habitats.models import Habitat

class HabitatSerializer(serializers.Serializer):
    class Meta:
        model = Habitat
        fields = ('name')

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Habitat` instance, given the validated data.
        """
        return Habitat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Habitat` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance