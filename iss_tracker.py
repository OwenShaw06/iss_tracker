import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

data = response.json()

print(type(data))
lat = data['iss_position']['latitude']
lon = data['iss_position']['longitude']
print(f"The ISS is currently at latitude {lat} and longitude {lon}.")