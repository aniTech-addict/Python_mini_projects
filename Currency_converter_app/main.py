from typing import Counter
from dotenv import load_dotenv

import currency_value_grabber as CV

def main():
    """
    1. Prints a welcome message.
    2. Asks the user to input an amount and the country names of the base and foreign currencies.
    3. Calls the currency_value function from the CV module to get the conversion rate.
    4. Prints the converted amount by multiplying the input amount with the conversion rate.
    
    """
    
    print("\n~~ Currency converter app ~~\n")
    
    base_currency_amount = int(input("Enter the Amount :").replace(',', ''))
    
    base_country_name = input("Enter the Base Currency country name :").strip()
    counter_country_name = input("Enter foreign Country name :").strip()

    counter_currency_value = CV.currency_value(base_country_name,counter_country_name)
    
    print(f"Value after Conversion = {base_currency_amount* counter_currency_value}")
    


if __name__ == '__main__':
    main()

