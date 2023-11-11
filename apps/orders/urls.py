from rest_framework.routers import DefaultRouter

from apps.orders.views import DriverOrdersViewSet, ClientOrdersViewSet

router = DefaultRouter()

router.register(prefix='driver-order', viewset=DriverOrdersViewSet, basename='driver-order')
router.register(prefix='client-order', viewset=ClientOrdersViewSet, basename='client-order')


urlpatterns = router.urls
