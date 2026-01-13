from django.urls import path
from .views import DishListView, DishCreateView, DishUpdateView, DishDeleteView

urlpatterns = [
    path('<int:menu_id>/dishes/', DishListView.as_view(), name='dish_list'),
    path('<int:menu_id>/dishes/create/', DishCreateView.as_view(), name='dish_create'),
    path('dishes/<int:pk>/edit/', DishUpdateView.as_view(), name='dish_update'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),
]
