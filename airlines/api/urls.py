from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name="homepage"), # Root domain
    path('airline/<str:pk>/', views.AirlineView, name="airline"), # airline listing
    path('aircraft/<str:pk>/', views.AirCraftView, name="aircraft"), # aircraft listing
    path('api-token-auth/', views.ApiTokenAuth, name="api-token-auth"), # api-token-auth
    path('airline/', views.AirlinesView, name="airlines"),
    path('aircraft/', views.AirCraftsView, name="aircrafts"),
    path('airline-create/',views.createAirline,name = "create-airline" ),
    path('aircraft-create/', views.createAircraft, name="create-aircraft"),
    path('airline-update/<str:pk>/', views.updateAirline,name="update-airline" ),
    path('aircraft-update/<str:pk>/', views.updateAircraft, name="update-aircraft"),
    path('airline-delete/<str:pk>/', views.deleteAirline, name="delete-airline"),
    path('aircraft-delete/<str:pk>/', views.deleteAircraft, name="delete-aircraft")
]