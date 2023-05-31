from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, EmailField


class MyProfileRetrieveUpdateSerializer(ModelSerializer):
    email = EmailField(read_only=True, max_length=64, )
    username = CharField(read_only=True, max_length=32, )

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    first_name = CharField(required=True, max_length=64, )
    last_name = CharField(required=True, max_length=64, )
    password = CharField(write_only=True, max_length=64, )

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'password'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user
