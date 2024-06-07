from django.db import models

class Dictionnary(models.Model):
    name = models.CharField(max_length=100)