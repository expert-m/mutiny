from django.db import models


class MailList(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=255)
