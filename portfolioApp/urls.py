from django.urls import path,include
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio', views.Portfolio_view, name='portfolio_view'),
]
