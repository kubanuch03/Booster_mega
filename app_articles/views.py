from rest_framework import permissions,generics

from app_articles.models import Articles

from .serializers import ArticlesSerializer

#User
class ArticleListsApiView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.AllowAny]

class ArticleDetailApiView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.AllowAny]




#Admin
class ArticlesCreateApiView(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAdminUser]

class ArticlesRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAdminUser]
