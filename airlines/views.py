from django.shortcuts import render
from django.http import HttpResponse

def Airline(request, pk):
    return HttpResponse(f'Airline number {pk}')

def AirCraft(request, pk):
    return HttpResponse(f'Aircraft {pk}')

def ApiTokenAuth(request):
    return HttpResponse('Api Token Authorization ')