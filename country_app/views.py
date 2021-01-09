from django.shortcuts import render
from django.http import HttpResponse
from .models import Country


# Create your views here.

def index(request):
    all_country_list = {'all_country': Country.objects.all()}
    return render(request, 'country_app/index.html', context=all_country_list)


def get_individual_country(request, a2c):
    res = Country.objects.filter(alpha2code=a2c)[0]
    print(res.name , res.population)
    country = {'individual_country': res}
    return render(request, 'country_app/get_individual_country.html', context=country)


def populate_country_data(request):
    return HttpResponse("Data is fetched and populated by scripts.py")
