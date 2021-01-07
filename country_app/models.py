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
    name = models.CharField(max_length=264, unique=True)
    capital = models.CharField(max_length=264, unique=True)
    population = models.BigIntegerField()
    timezones = models.CharField(max_length=264)
    language = models.CharField(max_length=264)
    neighbour = models.CharField(max_length=264)

    def __str__(self):
        return self.name


class LanguageList(models.Model):
    topic = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=264)

    def __str__(self):
        return self.language


class NeighbourList(models.Model):
    neighbour = models.CharField(max_length=264)

    def __str__(self):
        return set(self.neighbour)
