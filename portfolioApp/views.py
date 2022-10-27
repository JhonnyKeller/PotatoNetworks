from django.shortcuts import render
from .models import Portfolio,PortfolioCard


# Create your views here.
def Portfolio_view(request):
    portfolio = Portfolio.objects.all()
    portfoliocard = PortfolioCard.objects.all()

    return render(request, 'portfolio/portfolio.html', {'portfolio':portfolio,'portfoliocard':portfoliocard,})
