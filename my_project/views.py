from django.shortcuts import render
from .models import CountryData

def index(request):
    # Function to get top 10 countries for a given field
    def get_top_countries(field):
        return CountryData.objects.order_by('-' + field)[:10]

    # Getting top countries for each category
    top_scores = get_top_countries('score')
    top_gdp = get_top_countries('gdp_per_capita')
    top_social_support = get_top_countries('social_support')
    top_life_expectancy = get_top_countries('healthy_life_expectancy')
    top_freedom = get_top_countries('freedom_to_make_life_choices')
    top_generosity = get_top_countries('generosity')
    top_corruption = get_top_countries('perceptions_of_corruption')
    top_cost_living = get_top_countries('cost_of_living_index')
    top_rent_index = get_top_countries('rent_index')
    top_cost_living_rent = get_top_countries('cost_of_living_plus_rent_index')
    top_groceries = get_top_countries('groceries_index')
    top_restaurant_price = get_top_countries('restaurant_price_index')
    top_purchasing_power = get_top_countries('local_purchasing_power_index')

    # Preparing data for charts
    def prepare_chart_data(top_countries, field):
        return {            'labels': [country.country_or_region for country in top_countries],
            'data': [getattr(country, field) for country in top_countries],
        }

    chart_data = {
        'score': prepare_chart_data(top_scores, 'score'),
        'gdp_per_capita': prepare_chart_data(top_gdp, 'gdp_per_capita'),
        'social_support': prepare_chart_data(top_social_support, 'social_support'),
        'healthy_life_expectancy': prepare_chart_data(top_life_expectancy, 'healthy_life_expectancy'),
        'freedom_to_make_life_choices': prepare_chart_data(top_freedom, 'freedom_to_make_life_choices'),
        'generosity': prepare_chart_data(top_generosity, 'generosity'),
        'perceptions_of_corruption': prepare_chart_data(top_corruption, 'perceptions_of_corruption'),
        'cost_of_living_index': prepare_chart_data(top_cost_living, 'cost_of_living_index'),
        'rent_index': prepare_chart_data(top_rent_index, 'rent_index'),
        'cost_of_living_plus_rent_index': prepare_chart_data(top_cost_living_rent, 'cost_of_living_plus_rent_index'),
        'groceries_index': prepare_chart_data(top_groceries, 'groceries_index'),
        'restaurant_price_index': prepare_chart_data(top_restaurant_price, 'restaurant_price_index'),
        'local_purchasing_power_index': prepare_chart_data(top_purchasing_power, 'local_purchasing_power_index'),
    }

    context = {
        'chart_data': chart_data,
    }

    return render(request, 'index.html', context)
