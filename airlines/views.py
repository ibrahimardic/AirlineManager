from django.shortcuts import render
from django.http import HttpResponse
from .models import Aircraft, Airline
from .forms import AirlineForm, AircraftForm

def Homepage(request):
    msg = 'Hello, you are on the homepage.'
    return render(request, 'airlines/homepage.html',{'message':msg})

def AirlinesView(request):
    airlines = Airline.objects.all()
    context = {'airlines': airlines}
    return render(request, 'airlines/airlines.html', context)


def AirlineView(request,pk):
    airlineObj = Airline.objects.get(id=pk)
    return render(request, 'airlines/airline.html', {'airlineObj': airlineObj})

def AirCraftView(request, pk):
    aircraftObj = Aircraft.objects.get(id=pk)
    return render(request, 'airlines/aircraft.html', {'aircraftObj':aircraftObj})

def AirCraftsView(request):
    aircrafts = Aircraft.objects.all()
    context = {'aircrafts': aircrafts}
    return render(request, 'airlines/aircrafts.html', context)

def ApiTokenAuth(request):
    return HttpResponse('Api Token Authorization ')

def createAirline(request):
    airline_form = AirlineForm()
    context = {'airline_form':airline_form}
    return render(request, "airlines/airline_form.html", context)

def createAircraft(request):
    aircraft_form = AircraftForm()
    context = {'aircraft_form':aircraft_form}
    return render(request, "airlines/aircraft_form.html", context)