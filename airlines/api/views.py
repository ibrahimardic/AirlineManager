from django.shortcuts import render, redirect
from django.http import HttpResponse
from airlines.models import Aircraft, Airline
from airlines.forms import AirlineForm, AircraftForm
from airlines.api.serializers import AircraftSerializer, AirlineSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


def Homepage(request):
    msg = 'You are on the homepage.'
    return render(request, 'airlines/homepage.html',{'message':msg})

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    return Response({"message": "User registered successfully"}, status=201)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({"error": "Invalid credentials"}, status=401)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "User logged out successfully"}, status=205)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['GET','POST']) # Default is GET
@permission_classes([IsAuthenticated])
def AirlinesView(request):

    if request.method == 'GET':
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)  # Ensure `many=True` for QuerySet serialization
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # IF not valid
    

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def AirlineView(request,pk):
    if request.method == 'GET':
        airlineObj = Airline.objects.get(id=pk)
        serializer = AirlineSerializer(airlineObj)
        return Response(serializer.data, status=200)
    
    elif request.method == 'PATCH':
        AirlineObj = Airline.objects.get(id=pk)
        serializer = AirlineSerializer(AirlineObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400) # IF not valid
    
    elif request.method == 'DELETE':
        airlineObj = Airline.objects.get(id=pk)
        airlineObj.delete()
        return Response(status=204) 

@api_view(['GET','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def AirCraftView(request, pk):
    if request.method == 'GET':
        aircraftObj = Aircraft.objects.get(id=pk)
        serializer = AircraftSerializer(aircraftObj)
        return Response(serializer.data, status=200)
    
    elif request.method == 'DELETE':
        aircraftObj = Aircraft.objects.get(id=pk)
        aircraftObj.delete()
        return Response(status=204)  # No content, no data returned
    
    elif request.method == 'PATCH':
        aircraftObj = Aircraft.objects.get(id=pk)
        serializer = AircraftSerializer(aircraftObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400) # IF not valid
    


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def AirCraftsView(request):
    if request.method == 'GET':
        aircrafts = Aircraft.objects.all()
        serializer = AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # IF not valid    
    

def ApiTokenAuth(request):
    return HttpResponse('Api Token Authorization ')