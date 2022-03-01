from decimal import Decimal
from itertools import product
from pyexpat import model
from rest_framework import serializers
from store.models import Cart, Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    class Meta: # A class defines how an instance of the class (i.e. an object) behaves while a metaclass defines how a class behaves.
        model = Product
        fields = ['id', 'title', 'unit_price', 'description', 'slug', 'inventory', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
  

    def calculate_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id =self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'items']








    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match. Try again')
    #     return data

        

