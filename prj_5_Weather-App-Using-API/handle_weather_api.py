import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_geo_location():
    
    """
    Takes a city name as user input and returns the JSON response from the 
    OpenWeatherMap Geocoding API. The response contains the geographic 
    coordinates of the city.

    Returns:
    dict: A dictionary containing the JSON response from the API
    """
    print("Enter city name -> ")
    city_name = input()
    
    base_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API key}"
    
    try:
        response = requests.get(base_url)
        status_code = response.status_code
        
        if status_code == 200:
            return response.json()
    
    except:
        pass
    
        


def get_weather_info():
    pass    