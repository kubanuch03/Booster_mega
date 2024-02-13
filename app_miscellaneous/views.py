from rest_framework import permissions, generics

from .serializers import GallerySerializer

from .models import(
    Gallery
)





#==== Gallery  ========================================================

#User
class GalleryListApiView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]



    




#====   ========================================================
