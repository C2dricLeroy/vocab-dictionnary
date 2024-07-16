from django.db import models
from django.contrib.auth.models import User


class PrivacySettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    share_progress = models.BooleanField(default=True)
    show_online_status = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.user.username} Privacy Settings"