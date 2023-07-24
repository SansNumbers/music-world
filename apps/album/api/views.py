import json
import os

import requests
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from apps.album.api.serializers import AlbumListSerializer
from apps.album.models import Album


class AlbumListAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = AlbumListSerializer
