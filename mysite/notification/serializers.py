# serializers.py
from rest_framework import serializers
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice


class NotificationSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()

    def create(self, validated_data):
        device = FCMDevice.objects.all().first()
        message = Message(notification=Notification(**validated_data))
        device.send_message(message)
        return validated_data
