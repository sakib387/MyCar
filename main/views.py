from django.shortcuts import render,HttpResponse

# Create your views here.
def lending_page(request):
    return render(request,"views/main.html")
