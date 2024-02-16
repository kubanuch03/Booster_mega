from rest_framework import permissions, generics,response, status
from drf_spectacular.utils import extend_schema,OpenApiParameter

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
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="Все Контакты",
        description=" Запрос на Все Контакты ",
        responses={200: ContactUsSerializer(many=True)},
        operation_id="list_contactus",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ContactUsCreateApiView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Создать Контакты",
        description=" Запрос на Создание Контакты ",
        responses={201: ContactUsSerializer()},
        operation_id="create_contactus",
        
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
#====   ContactUs  ========================================================

#User
class FAQListApiView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Все FAQ",
        description=" Запрос на Все FAQ ",
        responses={200: FAQSerializer(many=True)},
        operation_id="list_faq",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#==== Gallery  ========================================================

#User
class GalleryListApiView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Все Галереи",
        description=" Запрос на Все Галареи ",
        responses={200: GallerySerializer(many=True)},
        operation_id="list_gallery",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    




