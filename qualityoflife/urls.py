from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('my_project.urls')),  # Replace 'my_project' with your actual app name
    # Add more paths for other apps as needed
]
