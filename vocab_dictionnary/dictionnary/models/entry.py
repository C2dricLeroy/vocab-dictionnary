from django.db import models
from dictionnary.models import Dictionnary


class Entry(models.Model):
    name = models.CharField(max_length=100)
    traduction = models.CharField(max_length=200)
    dictionnary = models.ForeignKey(Dictionnary, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def get_display_name(id:int) -> str: 
        entry = Entry.objects.get(id=id)
        display_name = entry.name.capitalize()
        return display_name