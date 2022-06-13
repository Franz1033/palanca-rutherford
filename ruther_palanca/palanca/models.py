from email import message
from django.db import models

class Entry(models.Model):
    recipient = models.CharField(max_length=400, null=False)
    code_name = models.CharField(max_length=400, null=False)
    message = models.TextField(max_length=10000, null=False)

    def __str__(self):
        return f'Message for {self.recipient} by {self.code_name}'