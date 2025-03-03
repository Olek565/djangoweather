from django.shortcuts import render
from dotenv import load_dotenv, dotenv_values
import os

# Create your views here.
load_dotenv()

def home(request):
    import json
    import requests

    apiKey = os.getenv("AIRNOW_API")
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        apiRequest = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=5&API_KEY={apiKey}")
        try:
            api = json.loads(apiRequest.content)
        except json.JSONDecodeError as e:
            api = {"error": "Failed to parse JSON response"}
            print(f"JSON Error: {e}")  # Debugging
        except requests.exceptions.RequestException as e:
            api = {"error": "Failed to fetch API data"}
            print(f"Request Error: {e}")  # Debugging


        if api[0]["Category"]["Name"] == "Good":
            category_color = "good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_color = "moderate"
        elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_color = "unhealty"
        elif api[0]["Category"]["Name"] == "Very Unhealthy":
            category_color = "veryunhealty"
        elif api[0]["Category"]["Name"] == "Hazarduous":
            category_color = "hazarduous"



        return render(request, 'home.html', {'api': api, 'category_color': category_color})

    else:

        apiRequest = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY={apiKey}")
        try:
            api = json.loads(apiRequest.content)
        except json.JSONDecodeError as e:
            api = {"error": "Failed to parse JSON response"}
            print(f"JSON Error: {e}")  # Debugging
        except requests.exceptions.RequestException as e:
            api = {"error": "Failed to fetch API data"}
            print(f"Request Error: {e}")  # Debugging


        if api[0]["Category"]["Name"] == "Good":
            category_color = "good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_color = "moderate"
        elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_color = "unhealty"
        elif api[0]["Category"]["Name"] == "Very Unhealthy":
            category_color = "veryunhealty"
        elif api[0]["Category"]["Name"] == "Hazarduous":
            category_color = "hazarduous"



        return render(request, 'home.html', {'api': api, 'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})