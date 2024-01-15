from django.shortcuts import render
from .models import CountryData

def index(request):
    # Function to calculate composite score
    def calculate_composite_score(country):
        base_score = 0.6 * country.score
        adjusted_indices = (100 - country.rent_index) + (100 - country.cost_of_living_index) + \
                           (100 - country.cost_of_living_plus_rent_index) + (100 - country.groceries_index) + \
                           (100 - country.restaurant_price_index)
        indices_score = 0.4 * (adjusted_indices / 100)  # Divided by 500 because there are 5 indices
        local_score = 0.09 * (country.local_purchasing_power_index / 100)
        return base_score + indices_score + local_score

    # Get all countries and calculate their composite score
    all_countries = CountryData.objects.all()
    for country in all_countries:
        country.composite_score = calculate_composite_score(country)

    # Sort countries by the new composite score
    top_countries_by_composite_score = sorted(all_countries, key=lambda x: x.composite_score, reverse=True)[:10]

    # Preparing data for charts using composite score
    def prepare_chart_data(top_countries):
        return {
            'labels': [country.country_or_region for country in top_countries],
            'data': [country.composite_score for country in top_countries],
        }

    chart_data = {
        'composite_score': prepare_chart_data(top_countries_by_composite_score),
        # Other charts can be added here if needed
    }

    context = {
        'chart_data': chart_data,
        'top_countries_by_composite_score': top_countries_by_composite_score,
    }

    return render(request, 'index.html', context)
