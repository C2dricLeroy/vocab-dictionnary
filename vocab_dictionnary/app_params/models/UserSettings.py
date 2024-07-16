from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interface_language = models.ForeignKey('dictionnary.Languages', on_delete=models.SET_NULL, null=True, blank=True)
    default_dictionary = models.ForeignKey('dictionnary.Dictionary', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Settings"