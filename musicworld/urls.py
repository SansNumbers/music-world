from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spotify/', include('spotify_app.urls')),
    path('api/v1/', include('apps.user.api.urls')),
    path('api/v1/', include('apps.album.api.urls')),
    path('api/v1/', include('apps.artist.api.urls')),
    path('api/v1/', include('apps.track.api.urls')),
    path('api/v1/', include('apps.review.api.urls')),
]
