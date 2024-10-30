from app.models import *
from django import forms
class BusForms(forms.ModelForm):
    class Meta:
        model = Bus_table
        fields = '__all__'
class PassengersForms(forms.ModelForm):
    class Meta:
        model = Passengers
        fields = '__all__'
    

