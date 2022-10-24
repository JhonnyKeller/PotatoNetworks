from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.NavBar)
admin.site.register(models.Hero)
admin.site.register(models.About)

admin.site.site_header  =  "PotatoNetworks admin"
# admin.site.site_title  =  "Custom bookstore admin site"
# admin.site.index_title  =  "Custom Bookstore Admin"
