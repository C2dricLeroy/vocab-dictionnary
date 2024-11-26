from django.db import models
from .Dictionary import Dictionary


class Entry(models.Model):
    original_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=300, editable=False)
    translation = models.CharField(max_length=200)
    dictionaries = models.ManyToManyField('Dictionary', related_name='entries', blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('original_name', 'translation')

    def save(self, *args, **kwargs):
        self.display_name = f"{self.original_name} : {self.translation}"
        super().save(*args, **kwargs)
