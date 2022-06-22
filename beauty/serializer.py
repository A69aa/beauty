from rest_framework import serializers
from .models import PushNotifications
from .models import InteriorImage,WorksOfMastersImage


class PushNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotifications
        fields = '__all__'

class PushCreateUpdateDeleteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    message = serializers.CharField(min_length=10,max_length=500)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorImage
        fields = '__all__'


class InteriorImageUpdateDeleteSerializer(serializers.Serializer):
    image = serializers.ImageField(
        # upload_to='interiorImage',
        # max_length=254, blank=True, null=True
    )



class Image2Serializer(serializers.ModelSerializer):
    class Meta:
        model = WorksOfMastersImage
        fields = '__all__'


class worksOfMastersImageUpdateDeleteSerializer(serializers.Serializer):
    image = serializers.ImageField(
        # upload_to='worksOfMastersImage',
        # max_length=254, blank=True, null=True
    )
