from rest_framework import serializers
from .models import Reviews
from app_users.models import CustomUser

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id','full_name','subtitle','image','review_text']