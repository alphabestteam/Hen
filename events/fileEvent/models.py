from django.db import models
from users.models import User


class regularEvent(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('close', 'Close'),
        ('wait_response', 'Wait to Response'),
        ('wait_handle', 'Wait to Handle'),
    )
    id = models.IntegerField(primary_key=True)
    open_date = models.DateField()
    close_date = models.DateField()
    ser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='regular_event', null=True, blank=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='open'  
    )

    in_archives = models.BooleanField(default=False)
    users_names = models.ManyToManyField(User, related_name='regular_events')
    toyota = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.status == 'close':
            self.toyota = False
        else:
            self.toyota = True
        super().save(*args, **kwargs)

class EventWithFiles(regularEvent):
    upload_date = models.DateField()
    file = models.FileField(upload_to='file_uploads/')
    user_upload = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files', null=True, blank=True)

class chat(models.Model):
    pass

class eventWithChat(regularEvent):
    chat = models.OneToOneField(chat,on_delete=models.CASCADE,related_name='chat_event')

class message(models.Model):
    text = models.CharField(max_length=200)
    message_date = models.DateField()
    user_send = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    chat = models.ForeignKey(chat, on_delete=models.CASCADE, related_name='messages')

   

