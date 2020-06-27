# using pythong3
# getOpenWeather.py - Prints the weather for a location from the command line

APPID = 'ba79963bf3d8558f9bead3a166b1b34a'

import json, requests, sys
import re, pprint

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py San+Francisco, US')
    sys.exit()
location = ''.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (location, APPID)
response = requests.get(url)
# print(response.raise_for_status())
pprint.pprint(response.text)
# Load JSON data into a python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])
