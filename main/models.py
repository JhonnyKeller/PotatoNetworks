from django.db import models
from services.models import ServicesPages
from colorfield.fields import ColorField

# Create your models here.
class NavBar(models.Model):
    img = models.FileField(upload_to='logo_img')
    title = models.CharField(max_length=254, unique=True, blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.color

class Hero(models.Model):
    carousel_active = [
    ('active','active'),
    ('','not active'),
    ]
    service = models.ForeignKey(ServicesPages,related_name='home_button',on_delete=models.CASCADE,null=True,blank=True)
    hone = models.CharField(max_length=254, unique=True)
    htwo = models.TextField(default='0')
    caurosel = models.CharField(choices=carousel_active,max_length=254,default=carousel_active[1][1],blank=True)
    img = models.ImageField(upload_to='carousel_img', blank=True)

    def __str__(self):
        return self.hone

class About(models.Model):
    title = models.CharField(max_length=254,default='')
    img = models.FileField(upload_to='about_img')
    text = models.TextField()

    def __str__(self):
        return self.text
