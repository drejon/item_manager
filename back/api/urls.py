from django.urls import path #type:ignore
from .views import ItemAPI, ItemDetailAPI

urlpatterns = [
    path('items', ItemAPI.as_view(), name='item_list'),
    path('items/<int:item_id>', ItemDetailAPI.as_view(), name='item_detail'),
]