import requests

class Country:
  def __init__(self, name, alpha2code, capital , population, timezones, flag, languages, n_countries):
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
        response_list.append(Country(
            response[i]['name'],
            response[i]['alpha2Code'],
            response[i]['capital'],
            response[i]['population'],
            response[i]['timezones'],
            response[i]['flag'],
            response[i]['languages'],
            response[i]['borders']
        ))
    return response_list

if __name__ == '__main__':
    response = country_call()
    cunt = 1
    for i in response:
        print(cunt)
        cunt = cunt + 1
        print("name", i.name)
        print("Alpha2Code" , i.alpha2code)
        print("Capital" ,i.capital)
        print("Population" , i.population)
        print("Timezones" , i.timezones)
        print("Flag" , i.flag)
        print("Language" , i.languages)
        print("Neighbouring" , i.n_countries)

