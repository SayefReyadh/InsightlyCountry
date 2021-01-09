from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/<str:a2c>/', views.get_individual_country, name='country_detail'),
    path('country/delete/<str:a2c>/', views.delete_individual_country, name='delete_country_detail'),
    path('reset/', views.populate_country_data, name='populate_country_data'),
]
