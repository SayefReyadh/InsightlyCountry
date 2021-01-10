from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Country
from script import bulk_create_all_country


# Create your views here.

def home(request):
    all_country_list = {'all_country': Country.objects.all()}
    return render(request, 'country_app/home.html', context=all_country_list)


def index(request):
    all_country_list = {'all_country': Country.objects.all()}
    return render(request, 'country_app/all_country.html', context=all_country_list)


def get_country(request, a2c):
    country = Country.objects.filter(alpha2code=a2c)
    if country:
        country = {'individual_country': Country.objects.filter(alpha2code=a2c)[0]}
        return render(request, 'country_app/single_country.html', context=country)
    else:
        return HttpResponse("Information of Alpha2Code: " + a2c + " has not been found")


def update_country(request, a2c):
    if request.method == 'POST':
        country = Country.objects.filter(alpha2code=a2c)[0]
        country.name = request.POST["name"]
        country.capitol = request.POST["capitol"]
        country.population = request.POST["population"]
        country.timezones = request.POST["timezones"]
        country.language_list = request.POST["language"]
        country.neighbour_list = request.POST["neighbouring"]
        country.save()
        return redirect('/country/'+a2c+'/view')
    else:
        country = {'individual_country': Country.objects.filter(alpha2code=a2c)[0]}
        return render(request, 'country_app/update_country.html', context=country)


def delete_country(request, a2c):
    Country.objects.filter(alpha2code=a2c).delete()
    return redirect('/country')
    # return HttpResponse("Information of Alpha2Code: " + a2c + " has been deleted")


def create_country(request):
    if request.method=='POST':
        Country.objects.create(
            alpha2code=request.POST["alpha2code"],
            name=request.POST["name"],
            capital=request.POST["capitol"],
            population=int(request.POST["population"]),
            timezones=request.POST["timezones"],
            flag=request.POST["flag"],
            language_list=request.POST["language"],
            neighbour_list=request.POST["neighbouring"],
        )
        return redirect('/country')
    else:
        return render(request, 'country_app/create_country.html')



def populate_country_data(request):
    # Country.objects.all().delete()
    bulk_create_all_country()
    return redirect('/')
