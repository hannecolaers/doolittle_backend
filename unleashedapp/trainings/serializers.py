from rest_framework import serializers, status
from rest_framework.exceptions import APIException

class TrainingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    #serialized_obj = serializers.serialize('json', [ obj, ])