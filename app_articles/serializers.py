from rest_framework import serializers

from app_articles.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    date_created = serializers.DateField(read_only=True)

    class Meta:
        model = Articles
        fields = ["id","title","short_description","description","date_created"]