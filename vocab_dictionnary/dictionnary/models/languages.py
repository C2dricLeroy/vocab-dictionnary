from django.db import models


def search_language_by_id(language_id: int):
    return Languages.objects.get(id=id)


class Languages(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_code(self):
        return self.code

    def __str__(self):
        return self.name
