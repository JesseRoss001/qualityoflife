from django.db import models

class CountryData(models.Model):
    country_or_region = models.CharField(max_length=100)
    score = models.FloatField()
    gdp_per_capita = models.FloatField()
    social_support = models.FloatField()
    healthy_life_expectancy = models.FloatField()
    freedom_to_make_life_choices = models.FloatField()
    generosity = models.FloatField()
    perceptions_of_corruption = models.FloatField()
    cost_of_living_index = models.FloatField()
    rent_index = models.FloatField()
    cost_of_living_plus_rent_index = models.FloatField()
    groceries_index = models.FloatField()
    restaurant_price_index = models.FloatField()
    local_purchasing_power_index = models.FloatField()
    composite_score = models.FloatField()
    final_rank = models.IntegerField()

    def __str__(self):
        return self.country_or_region
