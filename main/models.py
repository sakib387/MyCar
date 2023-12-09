from django.db import models
from users.models import Profile,Location
import uuid
from . const import CARS_BRANDS,TRANSMISSION_OPTIONS
from .utils import user_listing_path
# Create your models here.

class Listing(models.Model):
    id=models.UUIDField(
        primary_key=True,default=uuid.uuid4,unique=True,editable=False
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    seller=models.ForeignKey(Profile,on_delete=models.CASCADE)
    brand=models.CharField(max_length=24,choices=CARS_BRANDS,default=None)
    model=models.CharField(max_length=64,default='')
    vin=models.CharField(max_length=20,default='')
    mileage=models.IntegerField(default=0)
    color=models.CharField(max_length=20,null=True)
    description=models.TextField(null=True)
    engine=models.CharField(max_length=25,default='')
    transmisson=models.CharField(max_length=25,choices=TRANSMISSION_OPTIONS,default=None)
    locaton=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to=user_listing_path,default='')
    
    def __str__(self):
        return f'{self.seller.user.username}\'s Listing'
    

class LikedListing(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)
    like_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'liked by {self.profile.user.username}'
    
     
