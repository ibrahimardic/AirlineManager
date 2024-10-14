from django.db import models
import uuid

class Airline(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key= True)
    name = models.CharField(max_length=100)
    callsign = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=3)  # IATA cod

    def __str__(self): # To see the name on table.
        return self.name

class Aircraft(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key= True, editable=False)
    manufacturer_serial_number = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    operator_airline = models.ForeignKey(Airline, related_name='aircrafts', on_delete=models.CASCADE)
    number_of_engines = models.IntegerField()

    def __str__(self):
        return self.model