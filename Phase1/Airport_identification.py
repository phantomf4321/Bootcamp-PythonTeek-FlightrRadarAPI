# Define our main tools:
from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()

# Definition of tools used in reading images
from PIL import Image
import requests
from io import BytesIO

# This library will be used to display images
from matplotlib import pyplot as plt

# Map tool
import folium

# Put ICAO of your airport in function:
airport = fr_api.get_airport(code = "")
airport_details = fr_api.get_airport_details(airport.icao)

# Set values:
details = airport_details['airport']['pluginData']['details']
position = airport_details['airport']['pluginData']['details']['position']
airportImages = airport_details['airport']['pluginData']['details']['airportImages']

'''
Step1:

name = ...
country = ...
city = ...

print("{} in: {} / {}".format(name, city, country))
'''


'''
Step2:
latitude = ...
longitude = ...
elevation = ...
'''

'''
Step3:
response = ...
response = requests.get(response)
img = Image.open(BytesIO(response.content))

plt.imshow(img,cmap='gray')
plt.show()
'''

'''
Step4:
zone = folium.Map(location=[latitude, longitude], zoom_start=10)
folium.Marker(location=[latitude, longitude], popup='Airport', icon=folium.Icon(icon='plane', prefix='fa')).add_to(zone)

# Display map
zone
'''




