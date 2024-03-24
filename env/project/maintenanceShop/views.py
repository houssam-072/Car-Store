from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializer import RatingSerializer, ShopSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Shop, Rating
from rest_framework.permissions import IsAuthenticated
from accounts.models import User

# Create your views here.
class Shops(GenericAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        return Shop.objects.all()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk = None):
        if pk is not None:
            try:
                shop = Shop.objects.get(pk =pk)
            except Shop.DoesNotExist:
                return Response({'error' : 'Shop Not Found'}, status= status.HTTP_404_NOT_FOUND)
            serializer = ShopSerializer(shop)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            shop_list = self.get_queryset()
            serializer = ShopSerializer(shop_list, many = True)
            return Response(serializer.data, status= status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            shop = Shop.objects.get(pk = pk)
        except Shop.DoesNotExist:
            return Response({'error': 'Shop not found'}, status=status.HTTP_404_NOT_FOUND)   
        shop.delete()
        return Response({'message': 'Shop deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class Rate(GenericAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()
    
    def post(self, request, pk):
        shop = Shop.objects.get(pk = pk)
        user_mail = request.user
        data = request.data

        user_rate = User.objects.get(id = user_mail.id)

        rate_data_final = {
            'user' : user_rate.id,
            'shop' : shop.id,
            'rating' : data['rating'],
            'comment': data['comment']
        }
        serializer = RatingSerializer(data= rate_data_final)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        rate_list = self.get_queryset()
        serializer = RatingSerializer(rate_list, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

