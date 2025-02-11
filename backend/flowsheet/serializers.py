from rest_framework import serializers
from objects.serializers.PropertySetSerializer import PropertyInfoSerializer
from flowsheet.models.WeatherData import WeatherData
from flowsheet.models.Controller import Controller
from flowsheet.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controller
        fields = '__all__'

    def update(self, instance, validated_data):
        """
        Retrigger calculations on update
        """
        update_weather = False
        recalculate_nodes = False

        if 'latitude' in validated_data and instance.latitude != validated_data['latitude']:
            update_weather = True
        if 'longitude' in validated_data and instance.longitude != validated_data['longitude']:
            update_weather = True
        if ("grid_emission_factor" in validated_data and instance.grid_emission_factor != validated_data["grid_emission_factor"]):
            recalculate_nodes = True

        instance = super().update(instance, validated_data)
        instance.save()

        if update_weather:
            instance.weather.update_weather_data(instance.latitude, instance.longitude)

        if recalculate_nodes:
            instance.recalculate_energy_ins()

        return instance


class WeatherDataSerializer(serializers.ModelSerializer):
    irradiance = PropertyInfoSerializer(read_only=True)
    temperature = PropertyInfoSerializer(read_only=True)
    wind_speed = PropertyInfoSerializer(read_only=True)
    humidity = PropertyInfoSerializer(read_only=True)
    
    class Meta:
        model = WeatherData
        fields = "__all__"

    def update(self, instance, validated_data):
        """
        Retrigger calculations on update
        """
        instance = super().update(instance, validated_data)
        instance.save()
        controller = instance.weather_controller
        instance.update_weather_data(controller.latitude, controller.longitude)
        return instance
