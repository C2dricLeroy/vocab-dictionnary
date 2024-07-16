from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    primary_color = models.CharField(max_length=7, help_text='Hex code for the primary color')
    secondary_color = models.CharField(max_length=7, help_text='Hex code for the secondary color')
    background_color = models.CharField(max_length=7, help_text='Hex code for the background color')
    text_color = models.CharField(max_length=7, help_text='Hex code for the text color')
    border_color = models.CharField(max_length=7, blank=True, null=True, help_text='Hex code for the border color (optional)')
    is_default = models.BooleanField(default=False, help_text='Indicates if this is the default theme')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
