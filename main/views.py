from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm
from users.froms import locationForm
# Create your views here.

def lending_page(request):
    return render(request,"views/main.html")

@login_required
def home_view(request):
    listing=Listing.objects.all()
    print(listing)
    context={
        'listing':listing
    }
    return render(request,"views/home.html",context)

@login_required
def list_view(request):
    if request.method=='POST':
        pass
    elif request.method=='GET':
        listing_form=ListingForm()
        location_form=locationForm()
    return render (request,'views/list.html',{'listing_form':listing_form,'location_form':location_form})