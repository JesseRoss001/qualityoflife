from django.shortcuts import render
from .models import CountryData
from django.http import JsonResponse

def your_view(request):
    # Query to get the top 10 countries based on overall rank
    top_countries = CountryData.objects.order_by('overall_rank')[:10].values('country_or_region', 'overall_rank')
    
    # Pass 'top_countries' to the template
    return render(request, 'index.html', {'top_countries': top_countries})
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
