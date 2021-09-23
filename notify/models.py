from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=125, null=False, default="Default Notification")
    message = models.TextField(null=False, blank=True)


class Channels(models.Model):
    TYPES_OF_CHANNELS = [
        ("SMS", "SMS"),
        ("WEB", "WEB"),
        ("EMAIL", "EMAIL")
    ]
    name = models.CharField(choices=TYPES_OF_CHANNELS, default=None, null=True)
    notify = models.ForeignKey(Notification, related_name="channels")


class Recipient(User):
    channels = models.ManyToManyField(Channels, related_name="recipient_channels")
    notifications = models.ForeignKey(Notification, related_name="recipient_notifications")


class NotificationTypes(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(blank=True)
    notify = models.ForeignKey(Notification, related_name="types")
