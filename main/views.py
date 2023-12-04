from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm
from users.froms import locationForm
from django.contrib import messages
from .filters import ListingFilter
# Create your views here.

def lending_page(request):
    return render(request,"views/main.html")

@login_required
def home_view(request):
    listing=Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listing)
    context={
        'listing':listing,
        'listing_filter':listing_filter
    }
    return render(request,"views/home.html",context)

@login_required
def list_view(request):
    if request.method=='POST':
         try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = locationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')
            else:
                raise Exception()
         except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method=='GET':
        listing_form=ListingForm()
        location_form=locationForm()
    return render (request,'views/list.html',{'listing_form':listing_form,'location_form':location_form})