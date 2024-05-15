import requests
from bs4 import BeautifulSoup
import re

def fahrenheit_to_celsius(fahrenheit):
    celsius = float(fahrenheit - 32) * 5 / 9
    return celsius

class Weather:
    baseUrl = 'https://weather.com/weather/today/l/'
        
    @staticmethod
    def poznan():
        url = f'{Weather.baseUrl}1108a003bf79909edc7407896d97bb090d8c65a959ed42213b3110629e057015'
        return Weather._fetch_temperature(url)
    
    @staticmethod
    def warsaw():
        url = f'{Weather.baseUrl}27b1fe76a58c2df8f5b7202d26fb56e79df7d85e5150cb5c71c0c7ba33f8df3f'
        return Weather._fetch_temperature(url)

    @staticmethod
    def gdanks():
        url = f'{Weather.baseUrl}9232d0f0d32720f51ed452f5c7641057e3c7da0084a5916148f0ebc10cb6498e'
        return Weather._fetch_temperature(url)

    @staticmethod
    def _fetch_temperature(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find('span', {'data-testid': 'TemperatureValue'})
        if element:
            temperature_string = element.get_text(strip=True)
            # Extract numerical value using regular expression
            temperature_value = re.search(r'\d+', temperature_string)
            if temperature_value:
                temp_value = int(temperature_value.group())  
                celsius_temp = fahrenheit_to_celsius(temp_value)
                rounded_temp = round(celsius_temp, 1)
                return rounded_temp
        return None

# create instances
temperature_poznan = Weather.poznan()
temperature_warsaw = Weather.warsaw()
temperature_gdanks = Weather.gdanks()

# print what needs to be printed :D
print("Temperature in Poznan:", temperature_poznan)
print("Temperature in Warsaw:", temperature_warsaw)
print("Temperature in Gdanks:", temperature_gdanks)