from django.contrib import admin

# Register your models here.
from .models import Country, Language, Neighbour

admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Neighbour)
