# Simple Weather Forecasting App

This is a simple terminal-based weather forecasting application that fetches weather data from the OpenWeatherMap API. It prompts the user to enter the name of a city and then displays the current weather conditions for that city.

## Features

- Fetches current weather data for any city.
- Displays temperature, weather conditions, and more.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Toji-Fushigoro/Weather-Forecast.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Weather-Forecast
    ```
3. Install the required dependencies:
    ```bash
    pip install requests
    ```

## Usage

1. Run the application:
    ```bash
    python WeatherForecastApp.py
    ```
2. Enter the name of the city when prompted.

## Example

```bash
What is the name of your city? London
    The weather in London is Clear
    The weather in London feels Sunny
    In which format would you like the temperature?(C/F)<--celsius or farenheit
    :/> c <--capital or small
    The temperature in London is 339.099
```

