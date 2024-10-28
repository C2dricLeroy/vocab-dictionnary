from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Country
import csv
import os

@receiver(post_migrate)
def load_countries(sender, **kwargs):
    if sender.name == 'dictionary':
        csv_file_path = os.path.join(os.path.dirname(__file__), 'data/countries.csv')

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                country_name = row['name']
                country_code = row['country']
                country_latitude = row['latitude']
                country_longitude = row['longitude']

                Country.objects.update_or_create(
                    code=country_code,
                    defaults={'name': country_name,
                              'code': country_code,
                              'latitude': country_latitude,
                              'longitude': country_longitude
                              }

                )
