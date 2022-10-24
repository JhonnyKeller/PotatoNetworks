from django.urls import path,include
from . import views

app_name = 'resume'

urlpatterns = [
    path('resume/',views.Resume,name='resume_view')
]
