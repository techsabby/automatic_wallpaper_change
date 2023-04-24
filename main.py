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
		print("if statment ran")
		sunset = data['sunset']
		sunset_hour = int(sunset[0] + sunset[1]) - 4
		sunset_hour = sunset_hour + 12 # set hour to be in 24 hour format 
		sunset_minute = int(sunset[3] + sunset[4])

		# set target time for wallpaper to change 
		target_time = datetime.datetime(now.year, now.month, now.day, sunset_hour, sunset_minute)

		while datetime.datetime.now() < target_time:
			print("waiting for target_time: " + str(target_time))
			print("the current time is: " + str(datetime.datetime.now()))
			time.sleep(60)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, "W:\\Backup\\Documents\\Wallpapers\\studioghibli.jpg", 0)

		# wait until midnight to call function again 
		while datetime.datetime.now().hour > 0:
			print("waiting for midnight, current hour is: " + str(datetime.datetime.now().hour))
			time.sleep(1200)

		change_wallpaper()
	else: # it is before noon / set day time wallpaper 
		print("else statement ran")
		sunrise = data['sunrise']
		sunrise_hour = int(sunrise[0] + sunrise[1]) - 4
		sunrise_minute = int(sunrise[3] + sunrise[4])

		# set target time for wallpaper to change 
		target_time = datetime.datetime(now.year, now.month, now.day, sunrise_hour, sunrise_minute)

		while datetime.datetime.now() < target_time:
			print("waiting for target_time: " + str(target_time))
			print("the current time is: " + str(datetime.datetime.now()))
			time.sleep(60)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, "W:\\Backup\\Documents\\Wallpapers\\uow8tl3r8sw41.jpg", 0)

		while datetime.datetime.now().hour < 12:
			print("waiting for noon, current hour is: " + str(datetime.datetime.now().hour))
			time.sleep(1200)

		change_wallpaper()

change_wallpaper()