from django.urls import path
from Accounts.api.views import UserListCreateApiView
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("User/",UserListCreateApiView.as_view(),name = "User"),
    path("Token/",TokenObtainPairView.as_view(),name = "Token_Obtain"),
    path("Token/Refresh/",TokenRefreshView.as_view(),name = "Token_Refresh")
]