from rest_framework import generics
from .serializers import NotificationSerializer


class SendNotificationView(generics.CreateAPIView):
    serializer_class = NotificationSerializer
