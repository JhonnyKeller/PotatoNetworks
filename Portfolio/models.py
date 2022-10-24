from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=254, unique=True)
    text = models.TextField()

class PortfolioCard(models.Model):
    website_status = [
        ('still in development','still in development'),
        ('on air','on air'),
        ('cancelled','cancelled'),
    ]
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=254, unique=True)
    status = models.CharField(choices=website_status,max_length=254,default=website_status[0][0])
    # Upload image with 900px for 500px
    img = models.FileField(upload_to='examples',blank=True)
    url_to_website = models.URLField(max_length=200)
