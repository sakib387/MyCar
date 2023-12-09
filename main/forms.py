from django import forms
from users.widgets import CustomPictureImageFieldWidget
from .models import Listing


class ListingForm(forms.ModelForm):
    image = forms.ImageField(widget=CustomPictureImageFieldWidget)

    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage',
                  'color', 'description', 'engine', 'transmisson', 'image'}