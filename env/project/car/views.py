import os
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializer import CarSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage
from django.conf import settings
import joblib
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Ai_tool.main import get_car_price
import json

# Create your views here.


class Cars(GenericAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()

    def post(self, request):
        data = request.data
        user = request.user
        print('hi',data['owner'])

        print('hi')
        final_car_data = {
            'car_name' : data['car_name'],
            'brand' : data['brand'],
            'model' : data['model'],
            'desc' : data['desc'],
            'city' : data['city'],
            'capacity' : data['capacity'],
            'doors' : data['doors'],
            'aircondition' : data['aircondition'],
            'transmition' : data['transmition'],
            'mechanics' : data['mechanics'],
            'fuel' : data['fuel'],
            'price' : data['price'],
            'year' : data['year'],
            'color' : data['color'],
            'millage' : data['millage'],
            'image' : data['image'],
            'owner' : data['owner']
        }
        serializer = self.serializer_class(data = final_car_data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk = None, email=None):
        if pk is not None:
            try:
                car = Car.objects.get(pk = pk)
            except Car.DoesNotExist:
                return Response({'error': 'car not found'}, status=status.HTTP_404_NOT_FOUND)   
            serializer = CarSerializer(car)
            return Response(serializer.data, status= status.HTTP_200_OK)
        elif email is not None:
            try:
                user = User.objects.get(email = email)
                user_id = user.id
                cars = Car.objects.filter(owner=user_id)
                serializer = CarSerializer(cars, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Car.DoesNotExist:
                return Response({'error': 'No cars found for this owner email'}, status=status.HTTP_404_NOT_FOUND)
        else:
            car_list =self.get_queryset()
            serializer = CarSerializer(car_list, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            product = Car.objects.get(pk = pk)
        except Car.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)   
        product.delete()
        return Response({'message': 'product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def price_car(request):
    if request.method == 'POST':
        # Get JSON data from request
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
        # Call the function to get the car price
        try:
            price = get_car_price(data)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        # Return the predicted price in JSON format
        return JsonResponse({"predicted_price": price})

    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
