from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NotificationSerializer, ReciepientSerializer, SendNotificationSerializer
from .models import Recipient, NotificationTypes, Channels
from .utils import send_notification

class Notification(APIView):
    serializer_class = (NotificationSerializer)

    #notification view crud
    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(request.GET)
        if serialized_data.is_valid():
            res = serialized_data.save()
            return Response(res, status=201)



class NotificationUpdate(APIView):
    serializer_class = (NotificationSerializer,)

    def patch(self, request, *args, **kwargs):
        Notification_obj = NotificationTypes.object.get(pk=kwargs['pk'])
        serialized_data = self.serializer_class(Notification_obj, request.data, partial=True)
        if serialized_data.is_valid():
            res = serialized_data.save()
            return Response(res, status=200)

    def delete(self, request, *args, **kwargs):
        Notification_obj = NotificationTypes.object.get(pk=kwargs['pk']).delete()
        res = self.serializer_class(Notification_obj)
        return Response(res, status=200)



class Reciepient(APIView):
    serializer_class = (ReciepientSerializer,)

    #add recipients
    def post(self, request):
        pass

    #add a recipient to a notification type
    def patch(self, request, *args, **kwargs):
        pass
    

class SendNotification(APIView):
    serializer_class = (ReciepientSerializer, )

    def post(self, request):
        recipients = Recipient.objects.filter(notification__id__in=request.post["notification_id"])

        # send notification to all recipients base on enabled channels
        send_notification.delay(recipients)
        res = self.serializer_class(recipients, many=True)
        return Response(res, status=200)
