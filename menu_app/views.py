
from io import BytesIO

import qrcode
import qrcode.image.svg
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from auth_app.models import RestaurantOwner
from menu_app.models import Menu



class RestaurantList(ListView):
    model = RestaurantOwner


class MenuList(ListView):
    model = Menu
    
    def get_queryset(self):
        restaurant = RestaurantOwner.objects.get(id=self.kwargs['restaurant_id'])
        queryset = Menu.objects.filter(restaurant=restaurant)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(MenuList,self).get_context_data(**kwargs)
        context['restaurant_id'] = self.kwargs['restaurant_id']
        if self.request.user.id == self.kwargs['restaurant_id']:
            context['logged_in'] = True
        else:
            context['logged_in'] = False
        return context


class MenuCreate(CreateView):
    model = Menu
    fields = ['itemName', 'itemCategory', 'itemPrice', 'itemDescription', 'itemImage']
    
    def get_context_data(self, **kwargs):
        context = super(MenuCreate,self).get_context_data(**kwargs)
        context['add_page'] = True
        return context

    def form_valid(self, form):
        form.instance.restaurant = self.request.user
        return super(MenuCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('menu_list', kwargs={'restaurant_id':self.request.user.id})


class MenuUpdate(UpdateView):
    model = Menu
    fields = ['itemName', 'itemCategory', 'itemPrice', 'itemDescription', 'itemImage']
    
    def get_success_url(self):
        return reverse_lazy('menu_list', kwargs={'restaurant_id':self.kwargs['restaurant_id']})


class MenuDelete(DeleteView):
    model = Menu
    
    def get_success_url(self):
        return reverse_lazy('menu_list', kwargs={'restaurant_id':self.kwargs['restaurant_id']})


class MenuQRCode(View):
    def get(self, request, **kwargs):
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make('http://127.0.0.1:8000/' + str(self.kwargs['restaurant_id']), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context = {"svg": stream.getvalue().decode()}
        return render(request, "menu_app/qr_code.html", context=context)
