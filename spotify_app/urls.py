from django.urls import path

from spotify_app.main import get_token, search_for_artist, get_songs_by_artist

urlpatterns = [
    path('', get_token),
    path('artist/', search_for_artist),
    path('artist/songs/', get_songs_by_artist),
]
