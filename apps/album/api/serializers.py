from rest_framework.serializers import ModelSerializer

from apps.album.models import Album


class AlbumListCreateSerializer(ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'
