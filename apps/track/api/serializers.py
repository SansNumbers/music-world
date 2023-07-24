from rest_framework.serializers import ModelSerializer

from apps.track.models import Track


class TrackListCreateSerializer(ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'
