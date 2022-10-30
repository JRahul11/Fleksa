
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from auth_app.models import RestaurantOwner
from menu_app.models import Menu
from django.shortcuts import render

# def temp(request):
#     records = RestaurantOwner.objects.all()
#     print(request.user)
#     print("HI In")
#     return render(request, 'auth_app/restaurantowner_list.html', context={'object_list':records})


# def restaurantList(request):
#     print(request.user)
#     restaurant = RestaurantOwner.objects.all()
#     return render(request, 'auth_app/restaurantowner_list.html', context={'object_list':restaurant})

class RestaurantList(ListView):
    model = RestaurantOwner

class MenuList(ListView):
    model = Menu
    
    def get_queryset(self):
        restaurant = RestaurantOwner.objects.get(id=self.kwargs['restaurant_id'])
        queryset = Menu.objects.filter(restaurant=restaurant)
        print(self.request.user)
        print(self.request.session)
        return queryset
    
    def get_context_data(self, **kwargs):
        print(self.request.user)
        context = super(MenuList,self).get_context_data(**kwargs)
        context['restaurant_id'] = self.kwargs['restaurant_id']
        return context

class MenuCreate(CreateView):
    model = Menu
    fields = ['itemName', 'itemCategory', 'itemPrice', 'itemDescription', 'itemImage']
    
    def get_context_data(self, **kwargs):
        context = super(MenuCreate,self).get_context_data(**kwargs)
        # context['restaurant_id'] = self.kwargs['restaurant_id']
        print(self.request.user)
        return context

class MenuUpdate(UpdateView):
    model = Menu
    fields = ['itemName', 'itemCategory', 'itemPrice', 'itemDescription', 'itemImage']
    
    def get_success_url(self):
        return reverse_lazy('menu_list', kwargs={'restaurant_id':self.kwargs['restaurant_id']})

class MenuDelete(DeleteView):
    model = Menu
    
    def get_success_url(self):
        return reverse_lazy('menu_list', kwargs={'restaurant_id':self.kwargs['restaurant_id']})
