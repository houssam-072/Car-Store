from django.urls import path
from .views import Shops, Rate
urlpatterns = [
    path('add-shop/', Shops.as_view(), name='add-shop' ),
    path('delete-shop/', Shops.as_view(), name='delete-shop' ),
    path('get-all-shop/', Shops.as_view(), name='get-all-shop' ),
    path('get-shop/<int:pk>', Shops.as_view(), name='get-shop' ),
    path('rate-shop/<int:pk>', Rate.as_view(), name='get-rate-shop' ),
    path('rate-shop-list', Rate.as_view(), name='get-rate-list' ),
]