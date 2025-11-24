from rest_framework.routers import DefaultRouter
from ShopEasy.api.v1.viewsets import ProductViewSet, OrderViewSet, PaymentTransactionViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payment-transactions', PaymentTransactionViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = router.urls