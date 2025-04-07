from django.urls import path #type:ignore
from .views.item.item import Item
from .views.item.item_detail import ItemDetail


urlpatterns = [
    path('items', Item.as_view(), name='item_list'),
    path('items/<int:item_id>', Item.as_view(), name='item_detail'),
    path('auth/google', ItemDetail.as_view(), name='google_login'),
]