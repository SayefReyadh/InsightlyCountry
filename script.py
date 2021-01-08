import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InsightlyCountry.settings')

import django
django.setup()


from country_app.models import Country
from country_app.service import country_call

if __name__ == '__main__':
    response = country_call()
    bulk = []
    Country.objects.all().delete()


    #Double looped used for the same task in script.py and country_app.service.py
    #Improvements needed

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

