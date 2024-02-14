from django.urls import path

from .views import EventListApiView


urlpatterns = [
    path('list/evenv/',EventListApiView.as_view(),name= 'list-event')
]