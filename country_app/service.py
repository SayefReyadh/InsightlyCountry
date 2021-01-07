import requests
# from django.db.models import Count

class Country:
    def __init__(self, name, alpha2code, capital, population, timezones, flag, languages, n_countries):
        self.name = name
        self.alpha2code = alpha2code
        self.capital = capital
        self.population = population
        self.timezones = timezones
        self.flag = flag
        self.languages = languages
        self.n_countries = n_countries


def country_call():
    response = requests.get('https://restcountries.eu/rest/v2/all').json()
    response_list = []
    for i in range(len(response)):
        lang_list = []
        for j in range(len(response[i]['languages'])):
            lang_list.append(response[i]['languages'][j]['name'])

        response_list.append(Country(
            response[i]['name'],
            response[i]['alpha3Code'],
            # Took aplha3code to map neighbours
            response[i]['capital'],
            response[i]['population'],
            str(response[i]['timezones']),
            response[i]['flag'],
            ' '.join(lang_list),
            ' '.join(response[i]['borders'])
        ))
    return response_list


# if __name__ == '__main__':
#     response = country_call()
#
#     # models.Country.objects.bulk_create(response)
#
#     cunt = 1
#     for i in response:
#         print(cunt)
#         cunt = cunt + 1
#         print("Name", i.name, type(i.name))
#         print("Alpha2Code", i.alpha2code, type(i.alpha2code))
#         print("Capital", i.capital, type(i.capital))
#         print("Population", i.population, type(i.population))
#         print("Timezones", i.timezones[2:-2], type(i.timezones))
#         print("Flag", i.flag, type(i.flag))
#         print("Language", i.languages, type(i.languages))
#         print("Neighbouring", i.n_countries, type(i.n_countries))
