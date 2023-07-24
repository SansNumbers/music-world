from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user.api.serializers import MyProfileRetrieveUpdateSerializer, UserCreateSerializer


class MyProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MyProfileRetrieveUpdateSerializer

    def get_object(self, *args, **kwargs):
        return self.request.user


class RegisterUserAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = self.serializer_class(user).data
        token_serializer = TokenObtainPairSerializer()
        token = token_serializer.get_token(user)
        response_data['auth_token'] = str(token.access_token)
        return Response(response_data, status=HTTP_201_CREATED)
