from django.http import Http404
from rest_framework import mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.users.models import User
from apps.users.serializers import UsersSerializer, UserCreateSerializer, UsersDetailSerializer, VerifyUsersSerializer, \
    ResetPasswordSerializer


class UsersViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                   mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'retrieve':
            return UsersDetailSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return self.permission_classes

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if request.user != instance:
                return Response('You cannot delete someone else`s account!')
            self.perform_destroy(instance)
            return Response('Account deleted successfully!')
        except Http404:
            raise NotFound(detail="Invalid token", code="invalid_token")  # todo to ask


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


class VerifyUsersAPIView(GenericAPIView):
    serializer_class = VerifyUsersSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(phone_number=serializer.data['phone_number'])
        user.is_verified = True
        user.save()
        return Response({"message": "Your phone number has been confirmed"}, status=status.HTTP_200_OK)


class ResetPasswordAPIView(GenericAPIView):
    serializer_class = ResetPasswordSerializer  # todo

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
