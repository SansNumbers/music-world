from rest_framework.generics import ListCreateAPIView

from apps.track.api.serializers import TrackListCreateSerializer
from apps.track.models import Track


class TrackListCreateAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = TrackListCreateSerializer
    queryset = Track.objects.all()
