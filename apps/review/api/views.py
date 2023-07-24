from rest_framework.generics import ListCreateAPIView

from apps.review.api.serializers import ReviewListCreateSerializer
from apps.review.models import Review


class ReviewListCreateAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = ReviewListCreateSerializer

    def get_queryset(self):
        return Review.objects.all()
        # return self.request.user.reviews
