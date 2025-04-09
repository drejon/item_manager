from django.urls import path, include #type:ignore
from .views.item.item import Item
from .views.item.item_detail import ItemDetail
from .views.auth.google_login import GoogleLogin

urlpatterns = [
    path('items', Item.as_view(), name='item_list'),
    path('items/<int:item_id>', Item.as_view(), name='item_detail'),
    path('auth/login', include('dj_rest_auth.urls')),  # login/logout/password/reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # signup
    # path('auth/', include('allauth.socialaccount.urls')),  # for Google
    path('auth/', GoogleLogin.as_view()),  # for Google
]