from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.users.models import User
from apps.users.serializers import UsersSerializers, UserCreateSerializer


class UsersViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                   mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializers
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return self.serializer_class


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    user = request.user
    user_data = {
        'id': user.id,
        'full_name': user.full_name,
        'phone_number': user.phone_number,
    }

    return Response(user_data)
