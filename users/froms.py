from django import forms
from .models import Location
from localflavor.us.forms import USZipCodeField


class locationForm(forms.ModelForm):
    
    zip_code = USZipCodeField(required=True)
    class Meta:
        model=Location
        fields="__all__"