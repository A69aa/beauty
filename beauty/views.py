from rest_framework import viewsets
from .models import PushNotifications,InteriorImage,WorksOfMastersImage
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import (PushCreateUpdateDeleteSerializer,
                         PushNotificationsSerializer,
                         ImageSerializer,
                         InteriorImageUpdateDeleteSerializer,
                         Image2Serializer,
                         worksOfMastersImageUpdateDeleteSerializer)



class PushNotificationsListAPIView(ListCreateAPIView):
    queryset = PushNotifications.objects.all()
    serializer_class = PushNotificationsSerializer


class PushCreateUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PushNotifications.objects.all()
    serializer_class = PushCreateUpdateDeleteSerializer
    lookup_field = 'id'



class InteriorImageListCreateAPIView(ListCreateAPIView):
    queryset = InteriorImage.objects.all()
    serializer_class = ImageSerializer


class InteriorImageUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = InteriorImage.objects.all()
    serializer_class = InteriorImageUpdateDeleteSerializer
    lookup_field = 'id'




class WorksOfMastersImageListCreateAPIView(ListCreateAPIView):
    queryset = WorksOfMastersImage.objects.all()
    serializer_class = Image2Serializer


class worksImageUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = WorksOfMastersImage.objects.all()
    serializer_class = worksOfMastersImageUpdateDeleteSerializer
    lookup_field = 'id'