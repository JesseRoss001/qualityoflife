from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.country_data_view, name='country_data'),
    path('switch/', views.switch_countries, name='switch_countries'),
    path('preferences/', views.preferences_view, name='preferences'),
    # Add your other paths here
]