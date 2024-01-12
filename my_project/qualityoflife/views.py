# views.py
from django.http import JsonResponse
import sys
import os

# Add the path of main.py to sys.path to import it
sys.path.append('/workspace/qualityoflife/my_project/qualityoflife')
import main

def custom_view(request):
    data = main.combine_csv_data()  # Call the function from main.py
    return JsonResponse(data, safe=False)  # Return data as JSON
