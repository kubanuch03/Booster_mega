from rest_framework import serializers

from .models import Gallery,ContactUs,FAQ





class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ['id','title','phone_number','is_agreed']



class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ['id','title','response',]

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ['id','image','to_show']