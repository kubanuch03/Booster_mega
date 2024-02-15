from rest_framework import permissions,generics
from drf_spectacular.utils import extend_schema,OpenApiParameter

from .serializers import ReviewsSerializer
from .models import Reviews



#User
class ReviewsListApiView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Все Отзывы",
        description=" Запрос на Все ОТзывы ",
        responses={200: ReviewsSerializer(many=True)},
        operation_id="list_reviews",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#Admin
class ReviewsCreateApiView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAdminUser]


class ReviewsRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAdminUser]
    