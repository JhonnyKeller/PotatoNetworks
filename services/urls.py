from django.urls import path,include
from . import views

app_name = 'services'

urlpatterns = [
    path('services_view', views.Services, name='services_view'),
]
