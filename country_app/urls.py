from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('populate_country_data/', views.populate_country_data, name='populate_country_data'),

]
