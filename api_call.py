import requests
import json

api_url = "https://api.sunrise-sunset.org/json?lat=40.7127768&lng=-74.005974"

response = requests.get(api_url)
api_json = response.json()
data = api_json.get("results")

# get hour and minute of sunrise 
sunrise = data['sunrise']
sunrise_hour = sunrise[0] + sunrise[1]
sunrise_hour = int(sunrise_hour) - 4
sunrise_min = sunrise[4] + sunrise[5]
sunrise_min = int(sunrise_min)

# get hour and minute of sunset 
sunset = data['sunset']
sunset_hour = sunset[0] + sunset[1]
sunset_hour = int(sunset_hour) - 4




print(sunrise_hour)









#~~~ Troubleshooting Code ~~~#
#print(api_json.values())
#print(api_json.get("results"))
#test = list(api_json.get("results"))
#print(test)
#print(api_json.keys())
#print(api_json.values())
#print(api_json)
#print(api_json["status"])
#print("Sunrise: " + data['sunrise'])