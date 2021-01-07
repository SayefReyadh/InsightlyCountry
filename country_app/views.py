from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'country_app/index.html', context={'name':'My Name is Sayef Reyadh'})

def help(request):
    help_dict = {'help_insert':'HELP PAGE'} 
    return render(request, 'country_app/help.html', context=help_dict)

