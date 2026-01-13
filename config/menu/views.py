# menu/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dish, Menu

class DishListView(ListView):
    model = Dish
    template_name = 'menu/dish_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        self.menu = Menu.objects.get(id=self.kwargs['menu_id'])
        return Dish.objects.filter(menu=self.menu)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu
        return context

class DishCreateView(CreateView):
    model = Dish
    fields = ['name', 'price', 'description', 'image']
    template_name = 'menu/dish_form.html'

    def form_valid(self, form):
        menu_id = self.kwargs['menu_id']
        menu = Menu.objects.get(id=menu_id)
        form.instance.menu = menu
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_id = self.kwargs['menu_id']
        context['menu'] = Menu.objects.get(id=menu_id)
        return context

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={'menu_id': self.object.menu.id})

class DishUpdateView(UpdateView):
    model = Dish
    fields = ['name', 'price', 'description', 'image']
    template_name = 'menu/dish_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.object.menu
        return context

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={'menu_id': self.object.menu.id})

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'menu/dish_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={'menu_id': self.object.menu.id})
