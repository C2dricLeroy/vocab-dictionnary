from django.db import models
from django.contrib.auth.models import User


class NotificationSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=False)
    sms_notifications = models.BooleanField(default=False)
    daily_summary_notifications = models.BooleanField(default=False)
    daily_reminder_notifications = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} Notification Settings"