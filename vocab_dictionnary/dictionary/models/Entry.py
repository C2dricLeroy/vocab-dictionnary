from django.db import models
from .Dictionary import Dictionary


class Entry(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=300, editable=False)
    translation = models.CharField(max_length=200)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
