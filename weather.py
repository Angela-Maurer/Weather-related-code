import urllib.request
import json
import os

api_endpoint = 'http://api.openweathermap.org/data/2.5/weather'
city = input ('Enter city name: ')
city = city.replace(' ', '+')

API_KEY = os.environ.get('apikey')

url = api_endpoint + '?q=' + city + '&appid=' + API_KEY

#print (url)

response = urllib.request.urlopen(url)
parseResponse = json.loads(response.read())
#print(parseResponse)

temp_kelvin = parseResponse['main']['temp']
temp_celsius = int(temp_kelvin - 273.15)

weather = parseResponse['weather'][0]['description']
print(weather, temp_kelvin, temp_celsius)
