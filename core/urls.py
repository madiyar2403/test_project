from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', ObtainAuthToken.as_view())
]
