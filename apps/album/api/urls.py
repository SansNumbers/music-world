from django.urls import path

from apps.album.api.views import AlbumListAPIView

urlpatterns = [
    path('albums/', AlbumListAPIView.as_view(), name='album_list')
]
