from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('countrycomparison/', views.country_comparison, name='country_comparison'),
  path('search_countries/', views.search_countries, name='search_countries'),
   path('get_all_countries/', views.get_all_countries, name='get_all_countries'),
    # Add your other paths here
]