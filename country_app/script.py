from country_app.models import Country
from .service import country_call

#DEBUG Needed ModuleNotFoundError: No module named 'country_app' for """from country_app.models import Country"""
#DEBUG ImportError: attempted relative import with no known parent package for """from .models import Country"""


if __name__ == '__main__':
    response = country_call()

    for i in response:
        Country.objects.create(
            alpha2code=i.alpha2code,
            name=i.name,
            capital=i.capital,
            population=i.population,
            timezones=i.timezones,
            flag=i.flag,
            language_list=i.languages,
            neighbour_list=i.n_countries
        )
