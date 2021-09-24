
from .models import Recipient, Channels

def send_mail(recipient, channels):
    #send mail to this recipient via its channels
    pass

def send_notification(recipients):
    for recipient in recipients:
        send_mail(recipient, recipient.channels)
    