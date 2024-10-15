from django.forms import ModelForm
from .models import Airline,Aircraft

class AirlineForm(ModelForm):
    class Meta:
        model = Airline
        fields =['name', 'callsign','founded_year', 'base_airport']

class AircraftForm(ModelForm):
    class Meta:
        model = Aircraft
        fields ='__all__'