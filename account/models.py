from urllib import request
from django.db import models
from asyncio.windows_events import NULL
from email.policy import default
from tkinter import CASCADE

# Create your models here.

class userRestDetailsdb(models.Model):
    full_name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=25, choices={
        ('male', 'male'),
        ('Female', 'female')
    })
    mobile = models.IntegerField(null=False)
    account = models.CharField(max_length=50, null=False)

class patientdb(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=25, choices={
        ('male', 'male'),
        ('Female', 'female')
    })
    address = models.CharField(max_length=500)
    aadhaar = models.FileField(null=False)
    img = models.ImageField(default=None, null=True)
    medHistory = models.CharField(max_length=500)
    transectionDone = models.FloatField(default=0)
    transectionDue = models.FloatField(default=0)
    billCopy = models.FileField(null=False)
    labReport = models.FileField(null=False)
    symptoms = models.CharField(max_length=500)

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
        else:
            return '\static\img\default.png'


