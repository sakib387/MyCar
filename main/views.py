from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def lending_page(request):
    return render(request,"views/main.html")

@login_required
def home_view(request):
    return render(request,"views/home.html")
