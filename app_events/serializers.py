from rest_framework import serializers

from .models import Events




class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ['id','title','type','image','extended_image','datetime','duration','speaker_name','free_spots']

        