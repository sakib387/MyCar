from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
