from rest_framework.generics import ListCreateAPIView

from apps.album.api.serializers import AlbumListCreateSerializer
from apps.album.models import Album


class AlbumListCreateAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = AlbumListCreateSerializer
    queryset = Album.objects.all()
