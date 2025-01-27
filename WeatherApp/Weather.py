import requests
from datetime import datetime

# api_key =


zip_code = int(input("Enter your zip code: "))
country_code = input("Enter country code: ")

def get_3_day_forecast(zip_code, country_code, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?zip={zip_code},{country_code}&units=imperial&cnt=24&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Get every 8th entry to get 3 days worth of forecast data
        forecast = data['list'][::8]
        for i, day in enumerate(forecast, start=1):
            date = datetime.fromtimestamp(day['dt']).strftime('%m/%d/%y')  # Correcting to access 'day'
            temp = day['main']['temp']
            description = day['weather'][0]['description']  # Correcting to access 'day'
            print(f"Day {i} - Date: {date}")
            print(f"Temperature: {temp}°F")
            print(f"Weather: {description}")
            print("-" * 30)
    else:
        print("Error fetching data")

# Call the function
get_3_day_forecast(zip_code, country_code, api_key)
