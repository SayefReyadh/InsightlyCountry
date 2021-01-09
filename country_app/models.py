from django.db import models


# Create your models here.


# name Uruguay <class 'str'>
# Alpha2Code URY <class 'str'>
# Capital Montevideo <class 'str'>
# Population 3480222 <class 'int'>
# Timezones ['UTC-03:00'] <class 'list'>
# Flag https://restcountries.eu/data/ury.svg <class 'str'>
# Language [{'iso639_1': 'es', 'iso639_2': 'spa', 'name': 'Spanish', 'nativeName': 'Español'}] <class 'list'>
# Neighbouring ['ARG', 'BRA'] <class 'list'>


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    alpha2code = models.CharField(max_length=264, unique=True)
    name = models.CharField(max_length=264)
    capital = models.CharField(max_length=264)
    population = models.BigIntegerField(blank=True)
    timezones = models.CharField(max_length=264, blank=True)
    flag = models.CharField(max_length=264, blank=True)
    language_list = models.CharField(max_length=264, blank=True)
    neighbour_list = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.name


#One to Many Relationship Needed
class Language(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=264)

    def __str__(self):
        return self.language_name

#One to Many Relationship Needed
class Neighbour(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    neighbour_name = models.CharField(max_length=264)

    def __str__(self):
        return set(self.neighbour_name)
