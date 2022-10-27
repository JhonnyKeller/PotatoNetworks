from django.shortcuts import render
from .models import portfolioDBNEW,portfolioCardDBNEW


# Create your views here.
def Portfolio_view(request):
    portfolio = portfolioDBNEW.objects.all()
    portfoliocard = portfolioCardDBNEW.objects.all()

    return render(request, 'portfolioAppTwo/portfolio.html', {'portfolio':portfolio,'portfoliocard':portfoliocard,})
