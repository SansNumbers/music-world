from django.urls import path

from spotify_app.main import search_for_artist, get_songs_by_artist, search_for_album, search_for_track

urlpatterns = [
    path('artists/search/', search_for_artist),
    path('albums/search/', search_for_album),
    path('tracks/search/', search_for_track),
    path('artist/songs/', get_songs_by_artist),
]
