# Generated by Django 5.0.4 on 2024-06-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='languages',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
