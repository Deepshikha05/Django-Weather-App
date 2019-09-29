from django.shortcuts import render
import json 
import requests
import ast

def home(request):
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=60176&distance=5&API_KEY=E5988E53-F48E-4474-BA18-F51F4245D669")
    a = api_request.content.decode("utf-8")
    try:
        api = api_request.content
    except Exception as e:
        api = "Error ..."

    # if api.Category.Name == "Good":
    #     category_description = "Gooood"
    #     category_color = "good"
    # elif api.Category.Name == "Moderate":
    #     category_description = "It is Moderate"
    #     category_color = "moderate"
    # elif api.Category.Name == "Unhealthy for Sensitive Groups":
    #     category_description = "If you are sensitive, you should hide NOW!"
    #     category_color = "sensitive"
    # elif api.Category.Name == "Unhealthy":
    #     category_description = "Unhealthy"
    #     category_color = "unhealthy"
    # elif api.Category.Name == "hazardous":
    #     category_description = "Hazardous"
    #     category_color = "hazardous"
    return render(request, 'home.html', {'api':a})
                # "category_description":category_description,
                # "category_color":category_color})

def about(request):
    return render(request, 'about.html', {})