import re
import sys
import requests
import os
import shutil
import json

from datetime import datetime
api_key = ""  # Replace with actual API key


def get_3_day_forecast(zip_code, country_code, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?zip={zip_code},{country_code}&units=imperial&cnt=24&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        request_time = datetime.now()
        forecast = extract_3_day_forecast(data)
        print_forecast(forecast)
        write_time = datetime.now()
        log_forecast_request(zip_code, request_time, write_time)
    else:
        print("Sorry, invalid API response")

def extract_3_day_forecast(data):
        # Get every 8th entry to get 3 days worth of forecast data
        forecast = data['list'][::8]
        extracted = []

        for i, day in enumerate(forecast, start=1):
            date = datetime.fromtimestamp(day['dt']).strftime('%m/%d/%y')  # Correcting to access 'day'
            temp = day['main']['temp']
            description = day['weather'][0]['description']  # Correcting to access 'day'
            extracted.append([date, temp, description])

        return extracted

def print_forecast(forecast):
        lines = []

        # Pretty print
        for i, (date, temp, description) in enumerate(forecast, start=1):
            lines.append(f"Day {i} - Date: {date}")
            lines.append(f"Temperature: {temp}°F")
            lines.append(f"Weather: {description}")
            lines.append("-" * 30)

        forecast_text = '\n'.join(lines)

        print(forecast_text)

        try:

            # Rotate the forecast files
            if os.path.exists('forecast2.txt'):
                shutil.move('forecast2.txt', 'forecast3.txt')  # move forecast2 to forecast3
            if os.path.exists('forecast1.txt'):
                shutil.move('forecast1.txt', 'forecast2.txt')  # move forecast1 to forecast2

            # write to file
            with open("forecast1.txt", "w") as f:
                f.write(forecast_text)
        except (OSError, IOError, ValueError, TypeError) as e:
            print("Could not write to file")


def log_forecast_request(zip_code, request_time, write_time, log_file='forecast_log.json'):
    log_entry = {
        "zip_code": zip_code,
        "time_requested": request_time.isoformat(),
        "time_written": write_time.isoformat()
    }

    # Open the file in append mode
    with open(log_file, 'a') as f:
        # If the file is empty, write a starting list, else append new log entry
        if f.tell() == 0:
            json.dump([log_entry], f, indent=4)
        else:
            f.seek(f.tell() - 1)  # Go back to overwrite the closing bracket
            f.write(',\n')
            json.dump(log_entry, f, indent=4)
            f.write('\n]')


def main():
    try:
        while True:
            user_input = input("Enter ZIP code: ").strip()

            if re.fullmatch(r'\d{5}', user_input):
                zip_code = user_input
                break
            else:
                print("Please enter a valid zip code.")

        while True:
            user_input = input("Enter 2-letter country code: ").strip()

            if re.fullmatch(r'[A-Za-z]{2}', user_input):
                country_code = user_input
                break
            else:
                print("Please enter a valid 2-letter country code.")

        get_3_day_forecast(zip_code, country_code, api_key)

    except KeyboardInterrupt as e:
        print("Program exited by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
