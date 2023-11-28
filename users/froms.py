from django import forms
from .models import Location
from localflavor.us.forms import USZipCodeField


class locationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(required=True)
    class Meta:
        model=Location
        fields="__all__"