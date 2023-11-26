from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing
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
        pass
    return render (request,'views/list.html',{})