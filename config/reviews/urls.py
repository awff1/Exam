from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path('dish/<int:dish_id>/create/', ReviewCreateView.as_view(), name='review_create'),
]
