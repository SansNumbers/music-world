from rest_framework.fields import BooleanField
from rest_framework.serializers import ModelSerializer

from apps.album.models import Album


class AlbumListSerializer(ModelSerializer):
    add = BooleanField(required=True)

    class Meta:
        model = Album
        fields = [
            'add',
        ]

    def create(self, validated_data):
        print(self.context['request'].spotify_data)
        # album = super(AlbumListSerializer, self).create(validated_data)
        # for item in validated_data:
        #     print(item)
