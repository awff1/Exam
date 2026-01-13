from django.urls import path
from .views import RestaurantListView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant_delete'),
]