from django.urls import path
from menu_app.views import *

urlpatterns = [

    # Menu Routing
    path('', RestaurantList.as_view(), name='restaurant_list'),
    
    path('<int:restaurant_id>', MenuList.as_view(), name='menu_list'),
    
    path('<int:restaurant_id>/addItem', MenuCreate.as_view(), name='menu_create'),
    
    path('<int:restaurant_id>/updateItem/<int:pk>', MenuUpdate.as_view(), name='menu_update'),
    
    path('<int:restaurant_id>/deleteItem/<int:pk>', MenuDelete.as_view(), name='menu_delete'),
    
]
