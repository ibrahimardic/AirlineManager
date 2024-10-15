from rest_framework import serializers
import uuid
from airlines.models import Airline, Aircraft  # Assuming models are defined elsewhere

class AirlineSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)  # 'primary_key=True' should be set in the model, not the serializer
    name = serializers.CharField(max_length=100)
    callsign = serializers.CharField(max_length=100)
    founded_year = serializers.IntegerField()
    base_airport = serializers.CharField(max_length=3)

    class Meta:
        model = Airline  # Ensure you have an Airline model
        fields = ['id', 'name', 'callsign', 'founded_year', 'base_airport']

    def __str__(self):  # To display the name in admin panel, typically done in the model
        return self.name


class AircraftSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)  # UUID is read-only and automatically generated
    manufacturer_serial_number = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    operator_airline = serializers.PrimaryKeyRelatedField(queryset=Airline.objects.all())  # Handling the ForeignKey field properly
    number_of_engines = serializers.IntegerField()

    class Meta:
        model = Aircraft  # Ensure you have an Aircraft model
        fields = ['id', 'manufacturer_serial_number', 'type', 'model', 'operator_airline', 'number_of_engines']

    def __str__(self):
        return self.model
