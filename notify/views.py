from django.shortcuts import render, 
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NotificationSerializer

class Notification(APIView):
    serializer_class = (NotificationSerializer)

    #notification view crud
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(request.GET)
        if serialized_data.is_valid():
            res = serialized_data.save()
            return Response(res, status=201)



class NotificationUpdate(APIView):
    serializer_class = (NotificationSerializer)

    def patch(self, request, *args, **kwargs):
        Notification_obj = Notification.object.get(pk=kwargs['pk'])
        serialized_data = self.serializer_class(Notification_obj, request.data, partial=True)
        if serialized_data.is_valid():
            res = serialized_data.save()
            return Response(res, status=200)

    def delete(self, request, *args, **kwargs):
        Notification_obj = Notification.object.get(pk=kwargs['pk']).delete()
        res = self.serializer_class(Notification_obj)
        return Response(res, status=200)



class Reciepient(APIView):
    serializer_class = (ReciepientSerializer,)

    def post(self, request):
        pass
    

class SendNotification(APIView):
    serializer_class = (SendNotificationSerializer, )

    def post(self, request):
        reciepients = Recipients.objects.filter(notification__id=request.post["notification_id"])
