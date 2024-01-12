# your_project_name/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('qualityoflife.urls')),  # Replace 'your_app_name' with the actual name of your Django app
    # You can add more paths here as needed
]
