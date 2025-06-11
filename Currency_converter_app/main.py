from dotenv import load_dotenv
from currency_value_grabber import get_exchange_value 
import json
import os

def main():
    
    print("\n~~ Currency converter app ~~\n")

    country_name = input("Enter Country Name")
    conversion_values = get_exchange_value(country_name)
    


if __name__ == '__main__':
    main()

