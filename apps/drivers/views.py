from rest_framework import mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from apps.drivers.models import Drivers, CarModels
from apps.drivers.serializers import DriversSerializers, CarModelsSerializers, DriverCreateSerializer


class DriversViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializers
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.action == 'create':
            return DriverCreateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return self.permission_classes


class CarModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                      mixins.DestroyModelMixin):
    queryset = CarModels.objects.all()
    serializer_class = CarModelsSerializers
    permission_classes = [IsAuthenticated]
