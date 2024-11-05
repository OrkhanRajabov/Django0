from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Api/",include("Employ.api.urls")),
    path("Auth/",include("Accounts.api.urls")),
]