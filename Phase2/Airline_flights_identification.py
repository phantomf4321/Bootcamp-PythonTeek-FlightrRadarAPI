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


flights = fr_api.get_flights("IRM")

flight = flights[0]
flight_details = fr_api.get_flight_details(flight)


aircraft = flight_details['aircraft']
airline = flight_details['airline']

if flight_details['airport']['origin'] != None:
    origin = flight_details['airport']['origin']['name']
else:
    origin = None

if flight_details['airport']['destination'] != None:
    destination = flight_details['airport']['destination']['name']
    destination_icao = flight_details['airport']['destination']['code']['icao']
else:
    destination = None


response = flight_details['aircraft']['images']['large']
for r in response:
  curr_response = requests.get(r['src'])
  img2 = Image.open(BytesIO(curr_response.content))

  # Show the loaded image
  #img2.show()

  plt.imshow(img2,cmap='gray')
  plt.show()


if airline != None:
    print(aircraft['model']['text'], ": ", airline['name'], "/", airline['code']['icao'])
    print("{} ----> {}".format(origin, destination))


airport = fr_api.get_airport(destination_icao)
distance = flight.get_distance_from(airport)

print("{}km".format(distance))
