from django.shortcuts import render
from .models import CountryData
from django.http import JsonResponse

def index(request):
    categories = [
        'overall_rank', 'score', 'gdp_per_capita', 'social_support', 
        'healthy_life_expectancy', 'freedom_to_make_life_choices', 
        'generosity', 'perceptions_of_corruption', 'cost_of_living_index', 
        'rent_index', 'cost_of_living_plus_rent_index', 'groceries_index', 
        'restaurant_price_index', 'local_purchasing_power_index'
    ]

    top_countries = {}
    for category in categories:
        top_countries[category] = list(CountryData.objects.all().order_by(f'-{category}')[:10].values('country_or_region', category))

    return render(request, 'index.html', {'top_countries': top_countries})
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
