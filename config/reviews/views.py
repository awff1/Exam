# reviews/views.py
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Review
from menu.models import Dish

class ReviewCreateView(CreateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        dish_id = self.kwargs['dish_id']
        dish = Dish.objects.get(id=dish_id)
        form.instance.dish = dish
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish'] = Dish.objects.get(id=self.kwargs['dish_id'])
        return context

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={'menu_id': self.object.dish.menu.id})
