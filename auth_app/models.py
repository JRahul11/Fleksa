from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomManager(BaseUserManager):

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        if other_fields.get('is_staff') is not True or other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True and is_superuser=True')
        
        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        
        if not email:
            raise ValueError(_('You should provide a email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

class RestaurantOwner(AbstractBaseUser, PermissionsMixin):
    restaurantName = models.CharField(max_length=100, unique=True, null=True, verbose_name='Restaurant Name')
    email = models.CharField(max_length=100, unique=True, null=True)
    password = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='media/RestaurantImages', null=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomManager()
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['password']
    
    class Meta:
        verbose_name_plural = 'Restaurant Owners'
    
    def __str__(self):
        return f'{self.email} {self.restaurantName}'
