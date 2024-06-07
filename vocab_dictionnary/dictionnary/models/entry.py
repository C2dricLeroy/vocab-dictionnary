from django.db import models
from dictionnary.models import Dictionnary


class Entry(models.Model):
    name = models.CharField(max_length=100)
    traduction = models.CharField(max_length=200)
    dictionnary_id = models.ForeignKey(Dictionnary, on_delete=models.CASCADE)