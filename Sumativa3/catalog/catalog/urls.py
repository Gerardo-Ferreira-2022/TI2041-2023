from django.contrib import admin
from django.urls import path, include
from api.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),
    path('api/' , api.urls)

]
