from django.shortcuts import render
from .models import CountryData
def index(request):
    # Function to calculate composite score
    def calculate_composite_score(country):
        base_score = 0.6 * country.score
        adjusted_indices = (100 - country.rent_index) + (100 - country.cost_of_living_index) + \
                           (100 - country.cost_of_living_plus_rent_index) + (100 - country.groceries_index) + \
                           (100 - country.restaurant_price_index)
        indices_score = 0.4 * (adjusted_indices / 500)  # Divided by 500 because there are 5 indices
        local_score = 0.09 * (country.local_purchasing_power_index / 100)
        return base_score + indices_score + local_score

    # Function to get top and bottom 10 countries for a given field
    def get_top_bottom_countries(field):
        return CountryData.objects.order_by('-' + field)[:10], CountryData.objects.order_by(field)[:10]

    # Get all countries and calculate their composite score
    all_countries = CountryData.objects.all()
    for country in all_countries:
        country.composite_score = calculate_composite_score(country)

    # Sort countries by the new composite score
    top_countries_by_composite_score, bottom_countries_by_composite_score = sorted(all_countries, key=lambda x: x.composite_score, reverse=True)[:10], sorted(all_countries, key=lambda x: x.composite_score)[:10]

    # Preparing data for charts using composite score
    def prepare_chart_data(top_countries, bottom_countries, field):
        return {
            'top_labels': [country.country_or_region for country in top_countries],
            'top_data': [getattr(country, field) for country in top_countries],
            'bottom_labels': [country.country_or_region for country in bottom_countries],
            'bottom_data': [getattr(country, field) for country in bottom_countries]
        }

    # Getting top and bottom countries for each category
    top_bottom_data = {}
    for field in ['score', 'gdp_per_capita', 'social_support', 'healthy_life_expectancy', 
                  'freedom_to_make_life_choices', 'generosity', 'perceptions_of_corruption',
                  'cost_of_living_index', 'rent_index', 'cost_of_living_plus_rent_index',
                  'groceries_index', 'restaurant_price_index', 'local_purchasing_power_index']:
        top_countries, bottom_countries = get_top_bottom_countries(field)
        top_bottom_data[field] = prepare_chart_data(top_countries, bottom_countries, field)
    
    context = {
        'chart_data': top_bottom_data,
        'top_countries_by_composite_score': top_countries_by_composite_score,
        'bottom_countries_by_composite_score': bottom_countries_by_composite_score,
    }

    return render(request, 'index.html', context)