from rest_framework import permissions, generics

from .serializers import (
    GallerySerializer,
    ContactUsSerializer,
    FAQSerializer

)
from .models import(
    Gallery,
    ContactUs,
    FAQ
)








#====   ContactUs  ========================================================

#User
class ContactUsListApiView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.AllowAny]


#====   ContactUs  ========================================================

#User
class FAQListApiView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]


#==== Gallery  ========================================================

#User
class GalleryListApiView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]



    




