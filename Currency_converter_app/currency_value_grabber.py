import os
import requests
from urllib import response
from dotenv import load_dotenv
from supported_country_codes import country_codes

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_exchange_value(country_name):
    if country_name.upper() not in country_codes:
        print("-------------------------------------------------\n"
              "Unsupported Country, Please recheck the spelling or Enter another Country Name"
              "\n-----------------------------------------------")
        return
    
    country_code = country_codes[country_name.upper()] 
    base_link = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{country_code}"

    try:
        response = requests.get(url=base_link)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code if 'response' in locals() else 'N/A'}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred while making the requests: {req_err}")
    return None

def main():
    print("This file is not to be called")
    
if __name__ == "__main__":
    main()
