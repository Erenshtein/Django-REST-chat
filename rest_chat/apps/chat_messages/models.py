from django.db import models


class ChatMessage(models.Model):
    """Database model for Message."""
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='Author Email', max_length=128)
    text = models.CharField(verbose_name='Message Text', max_length=100)
    created_ts = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)
    updated_ts = models.DateTimeField(verbose_name='Update Date', auto_now=True)

    class Meta:
        verbose_name = 'API Message'
        verbose_name_plural = 'API Messages'

    def __str__(self):
        return self.text
