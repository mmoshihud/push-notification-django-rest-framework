from django.urls import path
from .views import SendNotificationView

urlpatterns = [
    path("create/", SendNotificationView.as_view(), name="send-notification"),
]
