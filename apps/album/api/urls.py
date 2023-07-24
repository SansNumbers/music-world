from django.urls import path

from apps.album.api.views import AlbumListCreateAPIView

urlpatterns = [
    path('albums/', AlbumListCreateAPIView.as_view(), name='album_list')
]
