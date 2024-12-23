from django.db import models

from django.contrib.auth.models import User


class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    source_language = models.ForeignKey('Languages', related_name='source_dictionaries', on_delete=models.CASCADE)
    target_language = models.ForeignKey('Languages', related_name='target_dictionaries', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dictionaries", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
