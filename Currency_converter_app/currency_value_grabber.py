import os
import requests
from urllib import response
from dotenv import load_dotenv
from supported_country_codes import country_codes

load_dotenv()
API_KEY = os.getenv("API_KEY")

"""
-------------------FLOW OF THE CODE---------------------

1. Get the conversion rates for the home country -> currency_value()
2. Find the country code for the foreign country -> find_country_code()
3. If the country code is not found, return None 
4. If the conversion rates are not found, return None

""" 
    
    
def currency_value(home_country,foreign_country):
    """_summary_

    Args:
        home_country (_type_): The country name of the base currency
        foreign_country (_type_): The country name of the counter currency

    Returns:
        int: returns the counter currency value 
    """
    conversion_rates  = get_conversion_rates(home_country)
    
    foreign_country_code = find_country_code(foreign_country)
    
    if conversion_rates is None or foreign_country_code is None:
        return None
    
    return conversion_rates[foreign_country_code]
    
    
    
def find_country_code(country_name):
    """_summary_

    Args:
        country_name (_type_): The country name for which the code is to be found

    Returns:
        str: The country code for the given country name
    """
    if country_name.upper() not in country_codes:
        print("-------------------------------------------------\n"
              "Unsupported Country, Please recheck the spelling or Enter another Country Name"
              "\n-----------------------------------------------")
        return None
        
    return country_codes[country_name.upper()] 




def get_conversion_rates(home_country):
    """_Grab the conversion rates for the given home country

    Args:
        home_country (str): The country name of the base currency

    Returns:
        dict: A dictionary containing the conversion rates
    """
    
    country_code = find_country_code(home_country)
    if country_code is None:
        return None
    base_link = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{country_code}"

    try:
        response = requests.get(url=base_link)
        response.raise_for_status()
        
        return response.json()['conversion_rates']

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code if 'response' in locals() else 'N/A'}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred while making the requests: {req_err}")




def main():
    print("This file is not to be called")
    
if __name__ == "__main__":
    main()
