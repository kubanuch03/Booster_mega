from rest_framework import serializers
from .models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id','full_name','subtitle','review_text']