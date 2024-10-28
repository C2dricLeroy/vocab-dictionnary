from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Country, Languages
import csv
import os

@receiver(post_migrate)
def load_countries(sender, **kwargs):
    if sender.name == 'dictionary':
        csv_file_path = os.path.join(os.path.dirname(__file__), 'data/country_list.csv')

        with open(csv_file_path, newline='', encoding='latin1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                country_name = row['country_name']
                country_code = row['country_code_name']
                lang_name = row['lang_name'].strip()
                lang_code = row['lang_code'].strip()

                country, created = Country.objects.update_or_create(
                    code=country_code,
                    defaults={'name': country_name}
                )

                if lang_name and lang_code:
                    language, lang_created = Languages.objects.get_or_create(
                        code=lang_code,
                        defaults={'name': lang_name}
                    )

                    country.languages.add(language)
