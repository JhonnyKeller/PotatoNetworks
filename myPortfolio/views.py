from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'index.html'

class about(TemplateView):
    template_name = 'about.html'

class PrivacyPolicy(TemplateView):
    template_name = 'privacy_policy.html'
