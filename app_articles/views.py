from rest_framework import permissions,generics
from rest_framework import response

from app_articles.models import Articles
from drf_spectacular.utils import extend_schema,OpenApiParameter
from .serializers import ArticlesSerializer

#User
class ArticleListsApiView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Все Новости",
        description=" Запрос на Все Новости ",
        responses={200: ArticlesSerializer(many=True)},
        operation_id="list_articles",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class ArticleDetailApiView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная Новость",
        description="Получить детальную информацию Новость",
        responses={200: ArticlesSerializer()},
        operation_id="detail_article",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




#Admin
class ArticlesCreateApiView(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAdminUser]

class ArticlesRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAdminUser]
