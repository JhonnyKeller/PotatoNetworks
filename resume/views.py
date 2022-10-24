from django.shortcuts import render
from .models import Sumary,ProfessionalExperience,Education,Skills



# Create your views here.
def Resume(request):
    sumary = Sumary.objects.all()
    professionalexperience = ProfessionalExperience.objects.all()
    education = Education.objects.all()
    skills = Skills.objects.all()

    return render(request, 'resume/resume.html',{'sumary':sumary,'professionalexperience':professionalexperience,'education':education,
                                                 'skills':skills,})
