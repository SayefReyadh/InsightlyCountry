import os
from country_app.models import Country
from country_app.service import country_call
import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InsightlyCountry.settings')
django.setup()


def bulk_create_all_country():
    response = country_call()
    bulk = []
    if Country.objects.all():
        Country.objects.all().delete()

    # Double looped used for the same task in script.py and country_app.service.py
    # Improvements needed

    for i in response:
        bulk.append(
            Country(
                alpha2code=i.alpha2code,
                name=i.name,
                capital=i.capital,
                population=i.population,
                timezones=i.timezones,
                flag=i.flag,
                language_list=i.languages,
                neighbour_list=i.n_countries
            )
        )
    Country.objects.bulk_create(bulk)


if __name__ == '__main__':
    bulk_create_all_country()