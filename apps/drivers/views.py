from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.drivers.models import Drivers, CarModels
from apps.drivers.serializers import DriversSerializers, CarModelsSerializers


class DriversViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializers
    permission_classes = [IsAuthenticated]


class CarModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                      mixins.DestroyModelMixin):
    queryset = CarModels.objects.all()
    serializer_class = CarModelsSerializers
    permission_classes = [IsAuthenticated]
