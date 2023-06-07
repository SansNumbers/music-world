import json
import os

import requests
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from apps.album.api.serializers import AlbumListSerializer
from apps.album.models import Album


class AlbumListAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = AlbumListSerializer

    def get_queryset(self):
        return Album.objects.all()

    def post(self, request):
        spotify_response = requests.get(
            'https://api.spotify.com/v1/search?q=The Forever Story&type=album&limit=1',
            headers={
                "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}",
            }
        )
        json_spotify_response = spotify_response.content.decode('utf8').replace("'", '"')
        return Response(json.loads(json_spotify_response), status=HTTP_200_OK)

    # def get(self, request, *args, **kwargs):
    #     flask_response = requests.get(
    #         f'http://{os.environ.get("FLASK_URL_DOMAIN")}:{os.environ.get("FLASK_URL_PORT")}/',
    #         data=bytes(str(serialized_data), 'UTF-8'),
    #         headers={
    #             "Auth-sync": os.environ.get('SECRET_SYNC_KEY'),
    #         },
    #     )

# class RegisterUserAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     permission_classes = ()
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         response_data = self.serializer_class(user).data
#         token_serializer = TokenObtainPairSerializer()
#         token = token_serializer.get_token(user)
#         response_data['auth_token'] = str(token.access_token)
#         return Response(response_data, status=HTTP_201_CREATED)


# class AuditListAPIView(ListAPIView):
# permission_classes = (IsUserACompanyOwner, )
# serializer_class = AuditListSerializer

# def get_queryset(self):
#     return Audit.objects.filter(
#         company=self.request.user.owned_company
#     ).filter(
#         created_on__range=[self.request.query_params.get('start_date'), self.request.query_params.get('end_date')]
#     )

# def get(self, request, *args, **kwargs):
#     audits_queryset = self.get_queryset()
#     serialized_data = serialize("json", audits_queryset)
#     serialized_data = json.loads(serialized_data)
#     flask_response = requests.get(

#         f'http://flask:5000/',

#             FLASK_APP = flask_apps / app.py
#             FLASK_DEBUG = 1
#             FLASK_URL_DOMAIN = flask
#             FLASK_URL_PORT = 5000

#         data=bytes(str(serialized_data), 'UTF-8'),
#         headers={
#             "Auth-sync": os.environ.get('SECRET_SYNC_KEY'),
#         },
#     )
#     json_flask_response = flask_response.content.decode('utf8').replace("'", '"')
#     return Response(json.loads(json_flask_response), status=HTTP_200_OK)
