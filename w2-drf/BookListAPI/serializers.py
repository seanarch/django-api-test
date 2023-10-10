# from rest_framework import serializers 
# from .models import MenuItem 

# class MenuItemSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = MenuItem 
#         fields = ['id', 'title', 'price', 'inventory']

from rest_framework import serializers 

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField() 
    title = serializers.CharField(max_length=255) 