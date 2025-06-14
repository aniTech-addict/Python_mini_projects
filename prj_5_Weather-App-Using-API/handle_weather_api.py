import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

LIMIT = 5
def get_coordinates(city_name,state_name):
    
    """
    Takes a city name as param and returns the JSON response from the 
    OpenWeatherMap Geocoding API. The response contains the geographic 
    coordinates of the city.

    Returns:
    dict: A dictionary containing the JSON response from the API
    """
    
    base_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={LIMIT}&appid={API_KEY}"
    
    try:
        response = requests.get(base_url)
        
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)
        coordinate_details=  response.json()  # If no error, parse and return JSON
        
        for coordinate in coordinate_details:
            if state_name == coordinate['state']:
                lat,lon = coordinate['lat'],coordinate['lon']
                return [lat,lon]
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for city '{city_name}': {http_err} - Status code: {http_err.response.status_code}")
        
    except requests.exceptions.RequestException as req_err:  # For other network issues (DNS failure, connection refused, timeout)
        print(f"Network error occurred for city '{city_name}': {req_err}")
        
    except ValueError as json_err:  # If response.json() fails (e.g. response is not valid JSON)
        print(f"JSON parsing error for city '{city_name}': {json_err}")
        
    except Exception as e:  # For any other unexpected exceptions
        print(f"An unexpected error occurred for city '{city_name}': {e}")
    
    return None # indicate failure    
    
        


def get_weather_info(city_name,state_name):
    coordinates = get_coordinates(city_name,state_name)
    lat,lon = coordinates[0],coordinates[1]
    
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    
    # HTTP error handling   

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code if 'response' in locals() else 'N/A'}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred while making the requests: {req_err}")
    except ValueError as json_err:
        print(f"JSON parsing error: {json_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return None
            