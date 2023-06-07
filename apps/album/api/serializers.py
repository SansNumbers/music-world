from rest_framework.serializers import ModelSerializer

from apps.album.models import Album


class AlbumListSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Album
