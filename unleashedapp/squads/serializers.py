from rest_framework import serializers
from squads.models import Squad, Membership
from employees.serializers import EmployeeSerializer

class SquadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Squad
        fields = ('id', 'name')

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

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    squad = SquadSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = Membership
        fields = ('employee', 'squad')

    def create(self, validated_data):
        """
        Create and return a new `Membership` instance, given the validated data.
        """
        return Membership.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Membership` instance, given the validated data.
        """
        instance.squad_id = validated_data.get('squad_id', instance.squad_id)
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.save()
        return instance

class EmployeesInSquadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        fields = ('employee_id',)

    employee = EmployeeSerializer()

    def create(self, validated_data):
        """
        Create and return a new `Membership` instance, given the validated data.
        """
        return Membership.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Membership` instance, given the validated data.
        """
        instance.squad_id = validated_data.get('squad_id', instance.squad_id)
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.save()
        return instance
