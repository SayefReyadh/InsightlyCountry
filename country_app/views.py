from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
from .service import country_call
# Create your views here.

def index(request):
    return render(request, 'country_app/index.html', context={'name':'My Name is Sayef Reyadh'})

def help(request):
    help_dict = {'help_insert':'HELP PAGE'}
    return render(request, 'country_app/help.html', context=help_dict)

def populate_country_data(request):
    res = country_call()

    for i in res:
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
    #Need some improvements using bulk_create

    return HttpResponse("Data is fetched and populated")
