from django import forms
from .models import Location
from localflavor.us.forms import USZipCodeField
from .models import Profile,User

class LocationForm(forms.ModelForm):
    
    zip_code = USZipCodeField(required=True)
    class Meta:
        model=Location
        fields="__all__"

class ProfileForm(forms.ModelForm):
    #photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')
    

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')