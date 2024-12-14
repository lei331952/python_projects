'''
Calculate the distance between two cities.
Allow the user to specify the unit of distance
Need to find lat long
'''
# pip install geopy

from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def geocode_city(city_name):
    geolocator = Nominatim(user_agent="city_geocoder")

    location = geolocator.geocode(city_name)

    if location:
        return {
            "city": city_name,
            "latlon": (location.latitude, location.longitude),
            "address": location.address
        }
    else:
        return {
            "error": f"Could not geocode the city{city_name}"
        }


city_name1 = "San Jose, CA"
loc1 = geocode_city(city_name1)
print(loc1)
city_name2 = "San Francisco, CA"
loc2 = geocode_city(city_name2)
print(loc2)

distance = geodesic(loc1["latlon"], loc2["latlon"])
print(f"distance = {distance}")
