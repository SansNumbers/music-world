from rest_framework.serializers import ModelSerializer

from apps.review.models import Review


class ReviewListCreateSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
