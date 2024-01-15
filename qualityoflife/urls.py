from django.contrib import admin
from django.urls import path, include
from my_project.views import index  # Adjust the import path based on your project structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),  # Add this line for your homepage
    path('app/', include('my_project.urls')),  # Adjust this if necessary
    
]