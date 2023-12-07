from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
   path('login',views.login_page,name="login"),
   path('register',views.Register_page,name='register'),
   path('logout',views.logout_view,name='logout'),
   path('profile',views.profile_view,name="profile")
    
]
 