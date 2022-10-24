from .models import ServicesPages


def get_servicespages(request):
    return {'servicespages_global': ServicesPages.objects.all()}
