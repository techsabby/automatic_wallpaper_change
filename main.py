import time
import json
import requests
import datetime

# function calls itself forever 
def change_wallpaper():

	# get sunrise and sunset times 
	api_url = "https://api.sunrise-sunset.org/json?lat=40.7127768&lng=-74.005974"
	response = requests.get(api_url)
	api_json = response.json()
	data = api_json.get("results")

	# get current system time 
	now = datetime.datetime.now()

	if (now.hour >= 12): # it is after noon / set night time wallpaper 
		sunset = data['sunset']
		sunset_hour = int(sunset[0] + sunset[1]) - 4
		sunset_hour = sunset_hour + 12 # set hour to be in 24 hour format 
		sunset_minute = int(sunset[3] + sunset[4])

		# set target time for wallpaper to change 
		target_time = datetime.datetime(now.year, now.month, now.day, sunset_hour, sunset_minute)

		while datetime.datetime.now() < target_time:
			time.sleep(30)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, "W:\\Backup\\Documents\\Wallpapers\\studioghibli.jpg", 0)

		# testing / wait until midnight to call function again 
		while now.hour > 0:
			time.sleep(60)

		changewallpaper()
	else: # it is before noon / set day time wallpaper 
		sunrise = data['sunrise']
		sunrise_hour = int(sunrise[0] + sunrise[1]) - 4
		sunrise_minute = int(sunrise[3] + sunrise[4])

		# set target time for wallpaper to change 
		target_time = datetime.datetime(now.year, now.month, now.day, sunrise_hour, sunrise_minute)

		while datetime.datetime.now() < target_time:
			time.sleep(30)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, "W:\\Backup\\Documents\\Wallpapers\\uow8tl3r8sw41.jpg", 0)

		while now.hour < 12:
			time.sleep(60)

		changewallpaper()

change_wallpaper()

"""
now = datetime.datetime.now()
print(now.hour)
if (now.hour >= 12):
	print("It is after noon.")
else:
	print("It is before noon.")




def senario_a():
	print("Senario A ran")
	time.sleep(10)
	senario_b()

def senario_b():
	print("Senario B ran")
	time.sleep(10)
	senario_a()

senario_a()
"""