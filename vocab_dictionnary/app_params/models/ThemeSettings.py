from django.db import models
from django.contrib.auth.models import User


class ThemeSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Theme Settings"