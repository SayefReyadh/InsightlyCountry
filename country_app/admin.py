from django.contrib import admin

# Register your models here.
from .models import Country, LanguageList, NeighbourList

admin.site.register(Country)
admin.site.register(LanguageList)
admin.site.register(NeighbourList)
