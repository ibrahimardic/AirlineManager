from django.shortcuts import render
from django.http import HttpResponse

airlines_list = [
    {
    'id' :'1',
    'name': 'Pegasus',
    'callsign': 'PC',
    'founded_year' : 1990,
    'base_airport': 'SAW'
    }
]
aircrafts_list = [
    {
        'id':'1',
        'manufacturer_serial_number':'4629',
        'type':'Airbus',
        'model':'Airbus A319-132',
        'operator_airline':'1',
        'number_of_engines':2,

    }
]


def Homepage(request):
    msg = 'Hello, you are on the homepage.'
    return render(request, 'airlines/homepage.html',{'message':msg})

def Airlines(request):
    context = airlines_list
    return render(request, 'airlines/airlines.html', {'airlines':context})

def Airline(request,pk):
    Airline = None
    for i in airlines_list: 
        if i['id'] == pk: # Whatever is the primary key is equal to id val.
            Airline = i
    return render(request, 'airlines/airline.html', {'specific_airline': Airline})

def AirCraft(request, pk):
    AirCraft = None
    for i in aircrafts_list: 
        if i['id'] == pk:
            AirCraft = i
    return render(request, 'airlines/aircraft.html', {'aircraft':AirCraft})

def AirCrafts(request):
    context = aircrafts_list
    return render(request, 'airlines/aircrafts.html', {'aircrafts':context})

def ApiTokenAuth(request):
    return HttpResponse('Api Token Authorization ')