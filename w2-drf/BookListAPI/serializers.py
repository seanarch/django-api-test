# from rest_framework import serializers 
# from .models import MenuItem 

# class MenuItemSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = MenuItem 
#         fields = ['id', 'title', 'price', 'inventory']

# from rest_framework import serializers 

# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField() 
#     title = serializers.CharField(max_length=255) 
#     inventory = serializers.IntegerField()


from rest_framework import serializers 
from .models import MenuItem, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category 
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer): 
    # change inventory to stock
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField()
    category = CategorySerializer()
    class Meta: 
        model = MenuItem 
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)