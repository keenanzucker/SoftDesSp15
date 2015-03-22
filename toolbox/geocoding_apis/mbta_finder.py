"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
import pprint
from pprint import pprint
from pygeocoder import Geocoder
import ast


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    responseText = f.read()
    responseData = json.loads(responseText)
    #return pprint(responseData)
    return responseData["results"][0]["formatted_address"]
    #responseData = pprint.pformat(responseData)
    #return responseData

#print get_json("https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park")

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    results = Geocoder.geocode(place_name)
    return results[0].coordinates

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=" + str(latitude) + "&lon=" + str(longitude) + "&format=json"
    
    allStops = urllib.urlopen(url)
    stops = allStops.read()

    stops = ast.literal_eval(stops)

    distance = stops['stop'][0]['distance']
    name = stops['stop'][0]['stop_name']

    return (float(distance), name)

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    coordinates = get_lat_long(place_name)
    return get_nearest_station(coordinates[0], coordinates[1])


#Testing with some famous Boston Points of Interest

print find_stop_near("TD Garden")
print find_stop_near("Fenway Park")
print find_stop_near("Hynes Convention Center")    #Returns 0.0 distance because it is a T stop!!