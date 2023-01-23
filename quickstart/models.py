from django.db import models
from django.conf import settings

import datetime
# Create your models here.
class Todo(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField()
    done = models.BooleanField(default=False)
    date_created = models.DateField(default=datetime.datetime.now())
    date_completed = models.DateField(null=True, blank=True)
