from django.urls import path
from rest_framework import routers

from apps.users.views import UsersViewSet, VerifyUsersAPIView

router = routers.DefaultRouter()

router.register(prefix='users', viewset=UsersViewSet, basename='users')

urlpatterns = [
    path('verify_user/', VerifyUsersAPIView.as_view(), name='verify_user')
] + router.urls
