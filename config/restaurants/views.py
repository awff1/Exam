from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Restaurant

class RestaurantListView(ListView):
    model = Restaurant
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(menu__dishes__name__icontains=q)
            ).distinct()
        return qs


class RestaurantCreateView(CreateView):
    model = Restaurant
    fields = '__all__'
    success_url = '/'


class RestaurantUpdateView(UpdateView):
    model = Restaurant
    fields = '__all__'
    success_url = '/'


class RestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = '/'
