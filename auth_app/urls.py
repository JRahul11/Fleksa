from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='user_register'),
    path('login', UserLoginView.as_view(), name='user_login'),
    path('logout', UserLogoutView.as_view(), name='user_logout'),
]
