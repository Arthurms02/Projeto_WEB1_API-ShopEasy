from rest_framework import viewsets
from ShopEasy.models import Product, Order, PaymentTransaction, OrderItem
from ShopEasy.api.v1.serializers import ProductSerializer, OrderSerializer, PaymentTransactionSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = Product.all_objects.all()
        
        return queryset
    
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()

    def get_queryset(self):
        queryset = OrderItem.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = OrderItem.all_objects.all()
        
        return queryset
    
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = Order.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = Order.all_objects.all()
        
        return queryset
    
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class PaymentTransactionViewSet(viewsets.ModelViewSet):

    queryset = PaymentTransaction.objects.all()

    def get_queryset(self):
        queryset = PaymentTransaction.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = PaymentTransaction.all_objects.all()
        
        return queryset
    
    serializer_class = PaymentTransactionSerializer
    permission_classes = [IsAuthenticated]  