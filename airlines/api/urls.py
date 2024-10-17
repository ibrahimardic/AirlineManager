from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('', views.Homepage, name="homepage"), # Root domain
    path('airline/<str:pk>/', views.AirlineView, name="airline"), # airline listing
    path('aircraft/<str:pk>/', views.AirCraftView, name="aircraft"), # aircraft listing
    path('airline/', views.AirlinesView, name="airlines"),
    path('aircraft/', views.AirCraftsView, name="aircrafts"),
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.login_user, name='login_user'),
    path('api/logout/', views.logout_user, name='logout_user'),
    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('api-token-verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify token

    # path('airline-create/',views.createAirline,name = "create-airline" ),
    # path('aircraft-create/', views.createAircraft, name="create-aircraft"),
    # path('airline-update/<str:pk>/', views.updateAirline,name="update-airline" ),
    # path('aircraft-update/<str:pk>/', views.updateAircraft, name="update-aircraft"),
    # path('airline-delete/<str:pk>/', views.deleteAirline, name="delete-airline"),
    # path('aircraft-delete/<str:pk>/', views.deleteAircraft, name="delete-aircraft")
]