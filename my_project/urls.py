from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('countrycomparison/', views.country_comparison, name='country_comparison'),
    # Add your other paths here
]