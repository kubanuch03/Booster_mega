from rest_framework import permissions, generics
from drf_spectacular.utils import extend_schema,OpenApiParameter

from .models import Events
from .serializers import EventSerializer








#User
class EventListApiView(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]


    @extend_schema(
        summary="Все Ивенты",
        description="Все Ивенты",
        responses={200: EventSerializer()},
        operation_id="list_event",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
