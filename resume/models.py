from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Sumary(models.Model):
    title = models.CharField(max_length=254,blank=True)
    text = models.TextField(blank=True)
    age = models.PositiveIntegerField(blank=True)
    city = models.CharField(max_length=254,blank=True)
    Degree = models.CharField(max_length=254,blank=True)
    email = models.EmailField(default='0',max_length=254)
    website = models.CharField(max_length=254, blank=True)
    phone_number = PhoneNumberField(blank=True)
    texttwo = models.CharField(max_length=254,blank=True)
    textthree = models.CharField(max_length=254,blank=True, default='')

    def __str__(self):
        return self.title

class ProfessionalExperience(models.Model):
    title = models.CharField(max_length=254, unique=True)
    subtitle = models.CharField(max_length=254, blank=True)
    daterange = models.CharField(max_length=254, blank=True)
    text = models.TextField(default='')

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=254, unique=True)
    subtitle = models.CharField(max_length=254, blank=True)
    daterange = models.CharField(max_length=254, blank=True)
    text = models.TextField(default='')

    def __str__(self):
        return self.title

class Skills(models.Model):
    lvl_one_to_five = [
        ('50','50'),
        ('60','60'),
        ('70','70'),
        ('80','80'),
        ('90','90'),
        ('100','100'),
    ]
    title = models.CharField(max_length=254, unique=True)
    lvl = models.CharField(choices=lvl_one_to_five,max_length=254,default=lvl_one_to_five[0][0])

    def __str__(self):
        return self.title
