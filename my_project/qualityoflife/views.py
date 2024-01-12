from django.shortcuts import render
from .models import CountryData
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def country_data_view(request):
    countries = CountryData.objects.all().order_by('final_rank')[:10]
    data = list(countries.values())
    return JsonResponse(data, safe=False)

def switch_countries(request):
    # Logic to switch between top 10 and bottom 10 countries
    # Placeholder for now
    pass

def preferences_view(request):
    # Logic to handle preferences
    # Placeholder for now
    pass
