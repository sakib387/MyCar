from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .froms import UserForm,ProfileForm,LocationForm
from main.models import Listing,LikedListing
# Create your views here.
def login_page(request):
    if request.method=='POST':
        login_form=AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
             
            if user is not None:
                login(request,user)
                messages.success(
                    request, f'You are now logged in as {username}.')
                return redirect('home')
            else : messages.error(request, f'An error occured trying to login.')
        else:
            messages.error(request, f'An error occured trying to login.')
    elif request.method=='GET':
        login_form=AuthenticationForm()
    return render(request,'views/login.html',{'login_form':login_form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')

def Register_page(request):
    if request.method=='POST':
        register_form=UserCreationForm(request.POST)
        if register_form.is_valid():
            user=register_form.save()
            user.refresh_from_db()
            login(request,user)
            messages.success(
                request,f'User {user.username} registered successfully.'

            )
            return redirect('home')
        else :
            messages.error(request, f'An error occured trying to register.')
            return render(request,'views/register.html',{'register_form':register_form})
    if request.method=='GET':
        register_form=UserCreationForm()
        return render(request,'views/register.html',{'register_form':register_form})

@login_required
def profile_view(request):
    if request.method=='GET':
        user_listings=Listing.objects.filter(seller=request.user.profile)
        user_like_listings=LikedListing.objects.filter(profile=request.user.profile).all()
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=request.user.profile)
        location_from=LocationForm(instance=request.user.profile.location)
        return render(request,'views/profile.html',{'user_form':user_form,'profile_form':profile_form,'location_form':location_from,'user_listings':user_listings,'user_liked_listings':user_like_listings})
    if request.method=='POST':
        user_form=UserForm(request.POST,instance=request.user)
        user_like_listings=LikedListing.objects.filter(profile=request.user.profile).all()
        profile_form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        location_from=LocationForm(request.POST,instance=request.user.profile.location)
        if user_form.is_valid() and profile_form.is_valid() and location_from.is_valid():
            user_form.save()
            profile_form.save()
            location_from.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error Updating Profile!')
        return render(request,'views/profile.html',{'user_form':user_form,'profile_form':profile_form,'location_form':location_from,'user_liked_listings':user_like_listings})