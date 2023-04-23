import time
import json
import requests
import datetime
import ctypes

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
			time.sleep(60)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, "W:\\Backup\\Documents\\Wallpapers\\studioghibli.jpg", 0)

		# wait until midnight to call function again 
		while datetime.date.now().hour > 0:
			time.sleep(1200)

		changewallpaper()
	else: # it is before noon / set day time wallpaper 
		sunrise = data['sunrise']
		sunrise_hour = int(sunrise[0] + sunrise[1]) - 4
		sunrise_minute = int(sunrise[3] + sunrise[4])

		# set target time for wallpaper to change 
		target_time = datetime.datetime(now.year, now.month, now.day, sunrise_hour, sunrise_minute)

		while datetime.datetime.now() < target_time:
			time.sleep(60)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, "W:\\Backup\\Documents\\Wallpapers\\uow8tl3r8sw41.jpg", 0)

		while datetime.datetime.now().hour < 12:
			time.sleep(1200)

		changewallpaper()

change_wallpaper()