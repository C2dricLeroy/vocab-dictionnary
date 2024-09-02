from django.db import models
from .dictionnary import Dictionnary


class Entry(models.Model):
    name = models.CharField(max_length=100)
    traduction = models.CharField(max_length=200)
    dictionnary = models.ForeignKey(Dictionnary, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def get_display_name(self) -> str:
        display_name = f"{self.name} ({self.traduction})"
        return display_name