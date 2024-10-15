from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name="homepage"), # Root domain
    path('airline/<str:pk>/', views.AirlineView, name="airline"), # airline listing
    path('aircraft/<str:pk>/', views.AirCraftView, name="aircraft"), # aircraft listing
    path('api-token-auth/', views.ApiTokenAuth, name="api-token-auth"), # api-token-auth
    path('airline/', views.AirlinesView, name="api-token-auth"),
    path('aircraft/', views.AirCraftsView, name="api-token-auth"),
]