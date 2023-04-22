import requests
import json

api_url = "https://api.sunrise-sunset.org/json?lat=40.7127768&lng=-74.005974"

response = requests.get(api_url)
api_json = response.json()
data = api_json.get("results")

# get hour and minute of sunrise 
sunrise = data['sunrise']
sunrise_hour = int(sunrise[0] + sunrise[1]) - 4
sunrise_min = int(sunrise[3] + sunrise[4])

# get hour and minute of sunset 
sunset = data['sunset']
sunset_hour = int(sunset[0] + sunset[1]) - 4
sunset_minute = int(sunset[3] + sunset[4])

print("Sunrise hour: " + str(sunrise_hour))
print("Sunrise minute: " + str(sunrise_min))
print("Sunset hour: " + str(sunset_hour))
print("Sunset minute: " + str(sunset_minute))






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