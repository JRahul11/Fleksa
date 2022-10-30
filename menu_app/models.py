from django.db import models
from auth_app.models import RestaurantOwner

class Menu(models.Model):
    Categories = (
        ('Refreshments', 'Refreshments'),
        ('Fast Food', 'Fast Food'),
        ('Lunch Plate', 'Lunch Plate'),
        ('Dinner Plate', 'Dinner Plate'),
        ('Indian Food', 'Indian Food'),
        ('Chinese Food', 'Chinese Food'),
        ('Soft Drinks', 'Soft Drinks'),
    )
    restaurant = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name')
    itemCategory = models.CharField(max_length=100, choices=Categories,  null=True, blank=True, verbose_name='Category')
    itemPrice = models.IntegerField(null=True, blank=True, verbose_name='Price')
    itemImage = models.ImageField(upload_to='media/MenuImages', null=True, blank=True, verbose_name='Image')
    itemDescription = models.TextField(verbose_name='Description')
    
    class Meta:
        verbose_name_plural = 'Menu Items'
    
    def __str__(self):
        return f'{self.restaurant.restaurantName} {self.itemName}'