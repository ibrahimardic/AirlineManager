from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = AirlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airlines')

    context = {'airline_form':airline_form}
    return render(request, "airlines/airline_form.html", context)

def updateAirline(request,pk):
    airline = Airline.objects.get(id=pk)

    airline_form = AirlineForm(instance = airline)

    if request.method == 'POST':
        form = AirlineForm(request.POST, instance=airline)
        if form.is_valid():
            form.save()
            return redirect('airlines')
    
    context = {'airline_form':airline_form}
    return render(request, "airlines/airline_form.html", context)

def deleteAirline(request,pk):
    airline = Airline.objects.get(id=pk)

    if request.method == 'POST':
        airline.delete()
        return redirect('airlines')

    context = {'object': airline}
    return render(request,'airlines/delete_template.html',context )

def createAircraft(request):
    aircraft_form = AircraftForm()

    if request.method == 'POST':
        form = AircraftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircrafts')

    context = {'aircraft_form':aircraft_form}
    return render(request, "airlines/aircraft_form.html", context)

def updateAircraft(request, pk):
    aircraft = Aircraft.objects.get(id=pk)

    aircraft_form = AircraftForm(instance=aircraft)

    if request.method == 'POST':
        form = AircraftForm(request.POST, instance=aircraft)
        if form.is_valid():
            form.save()
            return redirect('aircrafts')
        
    context = {'aircraft_form':aircraft_form}
    return render(request, "airlines/aircraft_form.html", context)

def deleteAircraft(request, pk):
    aircraft = Aircraft.objects.get(id =pk)

    if request.method == 'POST':
        aircraft.delete()
        return redirect('aircrafts')

    context = {'object': aircraft}
    return render(request,'airlines/delete_template.html',context )

