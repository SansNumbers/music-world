from django.urls import path

from apps.artist.api.views import ArtistListCreateAPIView

urlpatterns = [
    path('artists/', ArtistListCreateAPIView.as_view(), name='artist_list')
]
