from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return render(request, 'airlines/homepage.html')

def Airline(request, pk=None):
    return render(request, 'airlines/airlines.html')

def AirCraft(request, pk):
    return render(request, 'airlines/aircrafts.html')

def ApiTokenAuth(request):
    return HttpResponse('Api Token Authorization ')