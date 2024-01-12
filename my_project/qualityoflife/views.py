# views.py
from django.http import JsonResponse
from .main import combine_csv_data  # Make sure the path here is correct

def custom_view(request):
    data = combine_csv_data()
    return JsonResponse(data, safe=False)