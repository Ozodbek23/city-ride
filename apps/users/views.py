from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.users.models import Users
from apps.users.serializers import UsersSerializers


class UsersViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                   mixins.DestroyModelMixin):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    user = request.user
    user_data = {
        'id': user.id,
        'first_name': user.first_name,
        'username': user.username,
    }

    return Response(user_data)
