from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name="homepage"), # Root domain
    path('airline/<str:pk>/', views.Airline, name="airline"), # airline listing
    path('aircraft/<str:pk>/', views.AirCraft, name="aircraft"), # aircraft listing
    path('api-token-auth/', views.ApiTokenAuth, name="api-token-auth"), # api-token-auth
    path('airline/', views.Airlines, name="api-token-auth"),
    path('aircraft/', views.AirCrafts, name="api-token-auth"),
]