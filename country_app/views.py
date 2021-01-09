from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
from script import bulk_create_all_country


# Create your views here.

def index(request):
    all_country_list = {'all_country': Country.objects.all()}
    return render(request, 'country_app/index.html', context=all_country_list)


def get_individual_country(request, a2c):
    country = Country.objects.filter(alpha2code=a2c)
    if country:
        country = {'individual_country': Country.objects.filter(alpha2code=a2c)[0]}
        return render(request, 'country_app/get_individual_country.html', context=country)
    else:
        return HttpResponse("Information of Alpha2Code: " + a2c + " has not been found")


def delete_individual_country(request, a2c):
    Country.objects.filter(alpha2code=a2c).delete()
    return HttpResponse("Information of Alpha2Code: " + a2c + " has been deleted")


def populate_country_data(request):
    bulk_create_all_country()
    return HttpResponse("Data is Reset")
