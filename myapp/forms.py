from django import forms
from . import models


# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = "__all__"