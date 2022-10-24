from django.shortcuts import render
from .models import Hero,About
from resume.models import Sumary,Skills

# Create your views here.
def Index(request):
    hero = Hero.objects.all()

    return render(request, 'main/index.html', {'hero':hero,})



def About_view(request):
    about = About.objects.all()
    sumary = Sumary.objects.all()
    skills = Skills.objects.all()

    return render(request, 'main/about.html', {'about':about,'sumary':sumary,'skills':skills})
