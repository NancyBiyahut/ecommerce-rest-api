from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from .models import *
from  products . models import *
# Create your views here.



class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , request):
        user = request.user
        return Response({'sucsess' : 'permission working'})
    
    def post(self , request):
        user = request.user
        cart,_ = Cart.objects.get_or_create(user = user , ordered = False)
        product = Product.objects.get(id= request.data.get('product'))
        price = product.price 
        quantity = request.data.get('quantity')
        cart_items = CartItems(cart = cart ,user = user , product = product , price = price , quantity = quantity)
        cart_items.save()
        return Response({'sucess' : 'items added to your cart'})
    
    def update(self , request):
        pass
    
    def delete(self , request):
        pass