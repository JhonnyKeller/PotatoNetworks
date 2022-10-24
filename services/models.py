from django.db import models

# Create your models here.
class ServicesPages(models.Model):
    hidden = models.BooleanField()
    title = models.CharField(max_length=254)
    titletwo = models.CharField(max_length=254,default='')
    text = models.TextField()
    texttwo = models.TextField(default='')
    img = models.ImageField(upload_to='about_img')

    def __str__(self):
        return self.title

class ServicesBox(models.Model):
    service = models.ForeignKey(ServicesPages,related_name='services_box',on_delete=models.CASCADE)
    title = models.CharField(max_length=254, unique=True)
    text = models.TextField()
    # the best resolution to the img is 100px for 100px
    img = models.ImageField(upload_to='about_img', blank=True)

    def __str__(self):
        return self.title

class ServicesPrice(models.Model):
    service = models.ForeignKey(ServicesPages,related_name='services_price',on_delete=models.CASCADE)
    title = models.CharField(max_length=254, unique=True)
    subtitle = models.CharField(max_length=254, default='')
    text = models.TextField()
    # the best resolution to the img is 100px for 100px
    img = models.ImageField(upload_to='about_img', blank=True)
    price = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.title
