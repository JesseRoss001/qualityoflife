# urls.py
from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('custom_endpoint/', views.custom_view, name='custom_endpoint'),
    re_path(r'^$', RedirectView.as_view(url='/custom_endpoint/', permanent=False)),  # Redirect root to custom_endpoint
]