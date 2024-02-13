from rest_framework import permissions,generics

from .serializers import ReviewsSerializer
from .models import Reviews



#User
class ReviewsListApiView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.AllowAny]


#Admin
class ReviewsCreateApiView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAdminUser]


class ReviewsRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAdminUser]
    