from handle_weather_api import get_weather_info

def main():
    city_name = input("Enter City name-> ")
    state_name = input("Enter State name-> ")
    
    get_weather_info(city_name,state_name)

    
if __name__ == "__main__":
    print("\n~~ Weather App ~~\n")    
    main()