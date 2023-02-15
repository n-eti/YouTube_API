from django.db import models
from authentication.models import User
# Create your models here.

class Reply(models.Model):
    user = models.ForeignKey(User, related_name = 'reply', on_delete=models.CASCADE)
    comment = models.ForeignKey(User, related_name = 'text', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)