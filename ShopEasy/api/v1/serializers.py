from rest_framework import serializers
from ShopEasy.models import Product, Order, PaymentTransaction, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['deleted_at']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ['deleted_at']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['deleted_at']


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        exclude = ['deleted_at']