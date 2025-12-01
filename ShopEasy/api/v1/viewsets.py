from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ShopEasy.models import Product, Order, PaymentTransaction, OrderItem
from ShopEasy.api.v1.serializers import ProductSerializer, OrderSerializer, PaymentTransactionSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = Product.all_objects.all()
        
        return queryset
    @action(detail=True, methods=['post'])
    def restore(self, request,pk=None):
        """
        Restaura um produto deletado
        POST /api/v1/products/{id}/restore/
        """
        try:
            product = Product.all_objects.get(pk=pk)
            
            if product.deleted_at is None:
                return Response({'error': 'Produto não está deletado.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Restaura o produto
            product.restore()
            serializer = self.get_serializer(product)
            return Response(
                {'message': 'Produto restaurado com sucesso.', 'data': serializer.data}, status=status.HTTP_200_OK
                )
        except Product.DoesNotExist:
            return Response({'error': 'Produto não encontrado.'}, status=status.HTTP_404_NOT_FOUND)


class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = OrderItem.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = OrderItem.all_objects.all()
        
        return queryset
    
    @action(detail=True, methods=['post'])
    def restore(self, request,pk=None):
        """
        Restaura um item de pedido deletado
        POST /api/v1/order-items/{id}/restore/
        """
        try:
            order_item = OrderItem.all_objects.get(pk=pk)
            
            if order_item.deleted_at is None:
                return Response({'error': 'Item de pedido não está deletado.'}, status=status.HTTP_400_BAD_REQUEST)
            order_item.restore()
            serializer = self.get_serializer(order_item)
            return Response(
                {'message': 'Item de pedido restaurado com sucesso.', 'data': serializer.data}, status=status.HTTP_200_OK
                )
        except OrderItem.DoesNotExist:
            return Response({'error': 'Item de pedido não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = Order.all_objects.all()
        
        return queryset
    
    @action(detail=True, methods=['post'])
    def restore(self, request,pk=None):
        """
        Restaura uma ordem deletada
        POST /api/v1/orders/{id}/restore/
        """
        try:
            order = Order.all_objects.get(pk=pk)
            
            if order.deleted_at is None:
                return Response({'error': 'Ordem não está deletada.'}, status=status.HTTP_400_BAD_REQUEST)
            order.restore()
            serializer = self.get_serializer(order)
            return Response(
                {'message': 'Ordem restaurada com sucesso.', 'data': serializer.data}, status=status.HTTP_200_OK
                )
        except Order.DoesNotExist:
            return Response({'error': 'Ordem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)


class PaymentTransactionViewSet(viewsets.ModelViewSet):

    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        queryset = PaymentTransaction.objects.all()

        show_deleted = self.request.query_params.get('showDeleted')

        if show_deleted:
            queryset = PaymentTransaction.all_objects.all()
        
        return queryset

    @action(detail=True, methods=['post'])
    def restore(self, request, pk=None):
        """
        Restaura uma transação deletada.
        POST /api/v1/payment-transactions/{id}/restore/
        """
        try:
            transaction = PaymentTransaction.all_objects.get(pk=pk)
            
            if transaction.deleted_at is None:
                return Response(
                    {'error': 'Esta transação não está deletada'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            transaction.restore()
            serializer = self.get_serializer(transaction)
            return Response(
                {'message': 'Transação restaurada com sucesso', 'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except PaymentTransaction.DoesNotExist:
            return Response(
                {'error': 'Transação não encontrada'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    