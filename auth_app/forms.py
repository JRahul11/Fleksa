from django import forms
from auth_app.models import RestaurantOwner

class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Password'}))
    
    class Meta:
        model = RestaurantOwner
        fields = ['email', 'password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RestaurantOwner
        fields = '__all__'
        widgets = {
            'restaurantName': forms.TextInput(attrs={'placeholder':'Restaurant Name'}),
            'email': forms.TextInput(attrs={'placeholder':'Email'}),
            'password': forms.TextInput(attrs={'placeholder':'Password','pattern':'.{4,}'}),
            'image': forms.FileInput(attrs={'placeholder':'Restaurant Image'})
        }