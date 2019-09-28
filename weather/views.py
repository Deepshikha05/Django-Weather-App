from django.shortcuts import render
import json 
import requests

def home(request):
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=60176&distance=5&API_KEY=E5988E53-F48E-4474-BA18-F51F4245D669")
    try:
        api = api_request.content
    except Exception as e:
        api = "Error ..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})