from django.db import models


class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    source_language_id = models.ForeignKey('Languages', related_name='source_dictionaries', on_delete=models.CASCADE)
    target_language_id = models.ForeignKey('Languages', related_name='target_dictionaries', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
