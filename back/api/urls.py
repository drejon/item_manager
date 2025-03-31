from django.urls import path #type:ignore
from .views import ItemListAPI, ItemDetailAPI

urlpatterns = [
    path('v1/items', ItemListAPI.as_view(), name='item_list'),
    path('v1/items/<int:item_id>', ItemDetailAPI.as_view(), name='item_detail'),
]