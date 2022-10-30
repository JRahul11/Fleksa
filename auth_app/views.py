from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from auth_app.forms import RegisterForm
from auth_app.models import RestaurantOwner



class UserRegisterView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('user_login')
    template_name = 'auth_app/restaurantowner_form.html'
    
    def form_valid(self, form):
        restaurantName = form.data['restaurantName']
        email = form.data['email']
        password = make_password(form.data['password'])
        image = self.request.FILES['image']
        RestaurantOwner.objects.create(
            restaurantName=restaurantName, 
            email=email, 
            password=password, 
            image=image)
        return super(UserRegisterView,self).form_valid(form)


class UserLoginView(LoginView):
    template_name = 'auth_app/login.html'
    fields = ['email', 'password']
    redirect_authenticated_user = True
    
    def get_form(self, form_class=None):
        form = super(UserLoginView, self).get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Email'})
        form.fields['password'].widget = forms.TextInput(attrs={'placeholder': 'Password'})
        return form
    
    def get_success_url(self):
        return reverse_lazy('menu_list', kwargs={'restaurant_id':self.request.user.id})


class UserLogoutView(LogoutView):
    next_page = 'restaurant_list'
