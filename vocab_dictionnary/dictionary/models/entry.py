from django.db import models
from .dictionnary import Dictionnary


class Entry(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=300, editable=False)
    traduction = models.CharField(max_length=200)
    dictionnary = models.ForeignKey(Dictionnary, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.display_name = self.get_display_name()
        super().save(*args, **kwargs)

    def get_display_name(self) -> str:
        return f"{self.name} ({self.traduction})"
