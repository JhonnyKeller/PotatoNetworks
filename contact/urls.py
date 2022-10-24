from django.urls import path,include
from . import views

app_name = 'contact'

urlpatterns = [
    path('contact_view/', views.Contact_view, name='contact_view'),
]
