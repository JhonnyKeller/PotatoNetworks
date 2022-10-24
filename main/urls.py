from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Index, name='index'),
    path('about_view/', views.About_view, name='about'),
]
