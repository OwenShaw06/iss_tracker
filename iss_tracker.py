import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

data = response.json()

print(type(data))
lat = data['iss_position']['latitude']
lon = data['iss_position']['longitude']
print(f"The ISS is currently at latitude {lat} and longitude {lon}.")

my_lat = 40.3641
my_lon = -111.7385

import requests
from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers
    lat1, lon1, lat2, lon2 = radians(lat1), radians(lon1), radians(lat2), radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

distance = calculate_distance(my_lat, my_lon, float(lat), float(lon))
print(f"The ISS is currently {distance:.0f} km away from you.")