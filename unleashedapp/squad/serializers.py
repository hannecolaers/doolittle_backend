from rest_framework import serializers
from squad.models import Squad

class SquadSerializer(serializers.Serializer):
    class Meta:
        model = Squad
        fields = ('name')

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Squad` instance, given the validated data.
        """
        return Squad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Squad` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance