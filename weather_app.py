# Weather App using OpenWeatherMap API
# Developed by Mehak Chopra

import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_weather():
    city = input("Enter city name: ")
    if city:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                print(f"\nCurrent weather in {city}: {temp}°C, {desc}")
            else:
                print("City not found!")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    else:
        print("Please enter a city name.")

def get_forecast():
    city = input("Enter city name: ")
    if city:
        try:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == "200":
                print(f"\n5-Day Forecast for {city}:")
                for forecast in data["list"]:
                    date = forecast["dt_txt"]
                    temp = forecast["main"]["temp"]
                    weather_desc = forecast["weather"][0]["description"]
                    print(f"{date}: {temp}°C, {weather_desc}")
            else:
                print("City not found!")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    else:
        print("Please enter a city name.")

def main():
    print("Weather App")
    print("1. Get Current Weather")
    print("2. Get 5-Day Forecast")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        get_weather()
    elif choice == '2':
        get_forecast()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
