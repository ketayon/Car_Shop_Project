from django.contrib.auth.models import User
from django import forms
from carshopapp.models import CarShop, Car

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CarShopForm(forms.ModelForm):
    class Meta:
        model = CarShop
        fields = ('name', 'phone', 'address', 'logo')

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('name', 'model', 'category', 'owner_name', 'year_issue', 'image', 'price')