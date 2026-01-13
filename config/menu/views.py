from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dish, Menu

class DishListView(ListView):
    model = Dish
    paginate_by = 10

    def get_queryset(self):
        menu_id = self.kwargs.get("menu_id")
        return Dish.objects.filter(menu_id=menu_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.get(pk=self.kwargs.get("menu_id"))
        return context


class DishCreateView(CreateView):
    model = Dish
    fields = '__all__'
    template_name = 'menu/dish_form.html'

    def get_initial(self):
        return {'menu': self.kwargs.get("menu_id")}

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={'menu_id': self.object.menu.id})


class DishUpdateView(UpdateView):
    model = Dish
    fields = '__all__'
    template_name = 'menu/dish_form.html'

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={'menu_id': self.object.menu.id})


class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'menu/dish_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={'menu_id': self.object.menu.id})
