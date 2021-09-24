

from django.urls import path
from . import views

urlpatterns = [
    path("notification", views.Notification.as_view(), name="notification"),
    path("notification/update/<int:pk>", views.NotificationUpdate.as_view(), name="update_notification"),
    path("recipient/", views.Reciepient.as_view(), name="reciepient"),
    path("send_notification/", views.SendNotification.as_view(), name="send_notification"),
    path("recipient/disable_channel/", views.ReciepientDisableCHannel.as_view(), name="disable_channel"),
]