from rest_framework import routers

from apps.users.views import UsersViewSet

router = routers.DefaultRouter()

router.register(prefix='users', viewset=UsersViewSet, basename='users')

urlpatterns = router.urls
