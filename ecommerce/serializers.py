from rest_framework import serializers
from .models import Product,Category,Brand

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields =[
            'brand',
            'name',
            'price',
            'description',
            'stock',
            'image',
            'size',
            'material',
            'category'
        ]   

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=[
            "name",
            "slug"  
        ]
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields= [
            "name",
            "logo",
            "description"
            "country"
        ]