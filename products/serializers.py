from rest_framework import serializers
from .models import *




class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeVariant
        fields = '__all__' 
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 
    


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    product_type = TypeSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        