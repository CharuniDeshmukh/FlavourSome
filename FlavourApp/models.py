from email import message
from django.db import models

# Create your models here.
class Item(models.Model):
    sno = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=450)
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='food_items/', default="")

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default="")
    mobile = models.IntegerField(default=0, null=True)
    password = models.CharField(max_length=30, default='')
    area = models.CharField(max_length=100, default='', null=True)
    city = models.CharField(max_length=100, default='', null=True)
    state = models.CharField(max_length=30, default='', null=True)
    areaPin = models.CharField(max_length=8, default='', null=True)

    def __str__(self):
        return self.email

class Feedback(models.Model):
    sno = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    mobile = models.IntegerField(default=None)
    message = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.email