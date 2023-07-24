from rest_framework.generics import ListCreateAPIView

from apps.artist.api.serializers import ArtistListCreateSerializer
from apps.artist.models import Artist


class ArtistListCreateAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = ArtistListCreateSerializer
    queryset = Artist.objects.all()
