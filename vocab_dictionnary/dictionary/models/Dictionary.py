from django.db import models


class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    source_language = models.ForeignKey('Languages', related_name='source_dictionaries', on_delete=models.CASCADE)
    target_language = models.ForeignKey('Languages', related_name='target_dictionaries', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
