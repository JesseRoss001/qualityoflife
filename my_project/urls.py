from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Add your other paths here
]