from rest_framework.routers import DefaultRouter
from ShopEasy.api.v1.viewsets import ProductViewSet, OrderViewSet, PaymentTransactionViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payment-transactions', PaymentTransactionViewSet)

urlpatterns = router.urls