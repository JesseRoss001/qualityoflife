# views.py
from django.http import JsonResponse
from .main import combine_csv_data

def custom_view(request):
    combined_data = combine_csv_data()
    return JsonResponse({'data': combined_data})