from django.urls import path
from .views import *

urlpatterns = [
    path('list/gallery/',GalleryListApiView.as_view(),name='list-gallery'),

    path('list/contact/',ContactUsListApiView.as_view(),name='list-contact'),
    path('create/contact/',ContactUsCreateApiView.as_view(),name='create-contact'),

    path('list/gaq/',FAQListApiView.as_view(),name='list-faq'),


]