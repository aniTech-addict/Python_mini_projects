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
            if state_name.lower() == coordinate['state'].lower():
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
    
    
    """
    Takes a city name and state name as params and returns the JSON response from the
    OpenWeatherMap API. The response contains weather information for the city.

    Returns:
    dict: A dictionary containing the JSON response from the API
    """
    coordinates = get_coordinates(city_name,state_name)
    if not coordinates:
        print(f"Could not get coordinates for {city_name}, {state_name}.")
        return None
    
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

def interpret_weather_data(weather_data):
    
    """
    Takes a JSON response from the OpenWeatherMap API as input and returns a
    human-readable summary of the current weather.

    Args:
        weather_data (dict): A dictionary containing the JSON response from the API

    Returns:
        str: A human-readable summary of the current weather
    """
    if not weather_data:
        return "Could not retrieve weather information."

    try:
        description = weather_data['weather'][0]['description']
        temp_kelvin = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        city = weather_data['name']

        # Convert temperature from Kelvin to Celsius and Fahrenheit
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_celsius * 9/5) + 32

        summary = ("~~\n"
            f"The current weather in {city} is {description}. \n"
            f"The temperature is {temp_celsius:.1f}°C ({temp_fahrenheit:.1f}°F). \n"
            f"Humidity is {humidity}%, and wind speed is {wind_speed} m/s."
        )
        return summary
    except KeyError as e:
        return f"Error parsing weather data: Missing key {e}. Raw data: {weather_data}"
    except Exception as e:
        return f"An unexpected error occurred during weather interpretation: {e}"
