from django.urls import path
from . import views

urlpatterns = [
    path('airline/<str:pk>/', views.Airline, name="airline"),
    path('aircraft/<str:pk>/', views.AirCraft, name="aircraft"),
    path('api-token-auth/', views.ApiTokenAuth, name="api-token-auth")
]