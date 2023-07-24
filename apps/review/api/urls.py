from django.urls import path

from apps.review.api.views import ReviewListCreateAPIView

urlpatterns = [
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review_list')
]
