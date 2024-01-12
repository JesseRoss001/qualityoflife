# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('custom_endpoint/', views.custom_view, name='custom_endpoint'),
]