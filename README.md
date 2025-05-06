# 3-Day Weather Forecast App

Fetch a 3-day weather forecast using the OpenWeatherMap API. CLI app that will be used to study secure software development design principles. This project has been hardened with client-side validation principles and error handling.

## Features 
- Retrieves a 3-day weather forecast based on ZIP code and country code.
- Logs details of each forecast request (ZIP, request time, write time) into a JSON file.
- Saves the forecast in a rotating text file (forecast1.txt, forecast2.txt, forecast3.txt).

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- OpenWeatherMap API key

## Usage
1. Get an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
2. Clone the repository and install dependencies:
   ```bash
   pip install requests
3. Add your API key to the api_key variable in the script.
4. Run the script:
   ```bash
   python Weather.py
5. Enter your zip code and country code when prompted.

## Log File:
- The request details are saved in a JSON file (`forecast_log.json`).
- Each entry contains:
  - `zip_code`: The entered ZIP code.
  - `time_requested`: The timestamp when the request was made.
  - `time_written`: The timestamp when the forecast was written to the text file.
 
### Tests

The project includes unit tests to verify that the application correctly handles various scenarios like valid and invalid ZIP codes, API responses, and file handling.

#### Test Cases

1. **test_valid_forecast_output**: 
   - Tests whether the forecast output includes day information and whether the forecast is saved correctly in `forecast1.txt`.

2. **test_invalid_zip_error**:
   - Tests whether the program handles an invalid ZIP code correctly, printing the appropriate error message.

3. **test_expected_data_structure_from_extract**:
   - Tests if the data returned from the API is structured as expected. The result should be a list of 3 items, each containing a date, temperature, and description.

4. **test_handling_of_bad_api_key**:
   - Tests if the program handles an incorrect API key gracefully, showing the correct error message.

#### Dependencies

- **unittest**: Python’s built-in library for unit testing.
- **io.StringIO**: Used to capture print statements for validation in tests.

You can run the tests using:
