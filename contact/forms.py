from django import forms
from django.forms import ModelForm
from .models import ContactDataTwo
from captcha.fields import ReCaptchaField

class  ContactForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ContactDataTwo
        fields = ['service','service_pack','date','schedule',
                  'email','phone_number','text','file','captcha']
