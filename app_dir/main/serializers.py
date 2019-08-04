from rest_framework import serializers
from .models import *


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = ('topic', 'value', 'time', 'name')


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('topic', 'value', 'time', 'name')


class ServiceRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRegistry
        fields = ('id', 'name', 'service_type')


class MailBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailBox
        fields = ('id', 'name', 'api')


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = ('id', 'name', 'api', 'fields', 'connection')


class InteractiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interactive
        fields = ('id', 'name', 'fields')
