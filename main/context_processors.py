from .models import NavBar


def get_navbar(request):
    return {'navbar': NavBar.objects.all()}
