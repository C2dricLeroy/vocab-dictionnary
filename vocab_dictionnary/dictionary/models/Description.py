from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Description(models.Model):
    entry = models.ForeignKey('Entry', related_name='descriptions', on_delete=models.CASCADE)
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Optionnel
    created_at = models.DateTimeField(auto_now_add=True)
