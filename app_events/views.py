from rest_framework import permissions, generics

from .models import Events
from .serializers import EventSerializer








#User
class EventListApiView(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
