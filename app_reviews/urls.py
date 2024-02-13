from django.urls import path
from .views import (
    ReviewsListApiView,
    ReviewsCreateApiView,
    ReviewsRUDApiView
)


urlpatterns = [
    
    path('list/reviews/',ReviewsListApiView.as_view(),name='list-reviews'),
    path('create/reviews/',ReviewsCreateApiView.as_view(),name='create-reviews'),
    path('rud/reviews/<int:pk>/',ReviewsRUDApiView.as_view(),name='rud-reviews')
]