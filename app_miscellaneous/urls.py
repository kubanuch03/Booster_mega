from django.urls import path
from .views import GalleryListApiView

urlpatterns = [
    path('list/gallery/',GalleryListApiView.as_view(),name='list-gallery')
]