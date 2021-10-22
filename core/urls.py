# core/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # profiles app
    path('', include('apps.profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
