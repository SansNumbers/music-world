from django.urls import path

from apps.track.api.views import TrackListCreateAPIView

urlpatterns = [
    path('tracks/', TrackListCreateAPIView.as_view(), name='track_list')
]
