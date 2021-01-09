from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country/', views.index, name='all_country'),
    path('country/<str:a2c>/view', views.get_country, name='country'),
    path('country/delete/<str:a2c>/', views.delete_country, name='delete_country'),
    path('country/create/', views.create_country, name='create_country'),
    path('country/create/success', views.success, name='create_country_success'),
    path('reset/', views.populate_country_data, name='populate_country_data'),
]
