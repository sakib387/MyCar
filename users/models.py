from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField,USZipCodeField

# Create your models here.
class Location(models.Model):
    address1=models.CharField(max_length=150,blank=True)
    address2=models.CharField(max_length=150,blank=True)
    city=models.CharField(max_length=50)
    state=USStateField(default="NY")
    zip_code=USZipCodeField(blank=True)
    def __str__(self):
        return self.address1

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(null=True)
    bio=models.CharField(max_length=140,blank=True)
    phone_number=models.CharField(max_length=12,blank=True)
    location=models.OneToOneField(Location,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.username