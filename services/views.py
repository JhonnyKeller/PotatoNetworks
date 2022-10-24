from django.shortcuts import render
from .models import ServicesPages,ServicesBox,ServicesPrice

# Create your views here.
def Services(request):
    servicespages = ServicesPages.objects.all()
    servicesbox = ServicesBox.objects.all()
    servicesprice = ServicesPrice.objects.all()

    if request.method == 'POST':
        servicesname = request.POST.get('service_name','0')

        servicespages = servicespages.filter(title__contains=servicesname)
        servicesbox = servicesbox.filter(service__title__contains=servicesname)
        servicesprice = servicesprice.filter(service__title__contains=servicesname)

    return render(request, 'services/services.html', {'servicespages':servicespages,'servicesbox':servicesbox,
                                                      'servicesprice':servicesprice,})
