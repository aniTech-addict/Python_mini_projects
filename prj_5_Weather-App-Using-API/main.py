from handle_weather_api import get_weather_info, interpret_weather_data

def main():
    city_name = input("Enter City name-> ")
    state_name = input("Enter State name-> ")
    
    weather_data = get_weather_info(city_name,state_name)
    weather_summary = interpret_weather_data(weather_data)
    print(weather_summary)

        
if __name__ == "__main__":
    print("\n~~ Weather App ~~\n")    
    main()
