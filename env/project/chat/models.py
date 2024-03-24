from django.db import models
from accounts.models import User

class Chat(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_chats')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_chats')
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default = False)

    objects = models.Manager()


    def __str__(self):
        return f"Chat between {self.receiver.get_full_name} and {self.recipient.get_full_name}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.get_full_name} in {self.chat}"
