from django.urls import path
from .views import Cars,price_car
urlpatterns = [
    path('add-car', Cars.as_view(), name= 'add-car'),
    path('get-car/', Cars.as_view(), name= 'get-all-car'),
    path('get-car/<int:pk>/', Cars.as_view(), name= 'get-car'),
    path('get-car/<str:email>/', Cars.as_view(), name='car-owner-detail'),
    path('delete_car/<int:pk>', Cars.as_view(), name= 'delete_car'),
    path('car-price/', price_car, name = 'price-car' )

    
]