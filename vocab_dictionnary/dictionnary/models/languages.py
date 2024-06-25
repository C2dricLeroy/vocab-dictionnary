from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

