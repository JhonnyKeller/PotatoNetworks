from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from services.models import ServicesPages
from datetime import date

# Create your models here.
class ContactDataTwo(models.Model):
    contact_status = [
    ('awaiting response','awaiting response'),
    ('responded','responded'),
    ('banned message','banned message'),
    ]
    service_packs = [
    ('Basic','Basic'),
    ('Standard','Standard'),
    ('Gold','Gold'),
    ('Custom','Custom'),
    ]
    schedule_choices = [
    ('Lisbon Time 08:00h','Lisbon Time 08:00h'),
    ('Lisbon Time 09:00h','Lisbon Time 09:00h'),
    ('Lisbon Time 10:00h','Lisbon Time 10:00h'),
    ('Lisbon Time 11:00h','Lisbon Time 11:00h'),
    ('Lisbon Time 12:00h','Lisbon Time 12:00h'),
    ('Lisbon Time 14:00h','Lisbon Time 14:00h'),
    ('Lisbon Time 15:00h','Lisbon Time 15:00h'),
    ('Lisbon Time 16:00h','Lisbon Time 16:00h'),
    ('Lisbon Time 18:00h','Lisbon Time 18:00h'),
    ]
    date = models.DateField(default=date.today)
    service = models.ForeignKey(ServicesPages,related_name='services_option',on_delete=models.CASCADE)
    service_pack = models.CharField(choices=service_packs,max_length=254,default=service_packs[0][0])
    email = models.EmailField(default='')
    phone_number = PhoneNumberField(blank=True)
    text = models.TextField(default='')
    status = models.CharField(choices=contact_status,max_length=254,default=contact_status[0][0])
    schedule = models.CharField(choices=schedule_choices,max_length=254,default=schedule_choices[0][0])
    file = models.FileField(upload_to='contact_files',blank=True)

    def __str__(self):
        return self.email
