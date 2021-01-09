from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
from .service import country_call


# Create your views here.

def index(request):
    all_country_list = {'all_country': Country.objects.all()}
    return render(request, 'country_app/index.html', context=all_country_list)

def populate_country_data(request):
    return HttpResponse("Data is fetched and populated by scripts.py")
