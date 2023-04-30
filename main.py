import time
import json
import requests
import datetime
import ctypes

# this program gets the sunrise and sunset times for your area 
# via an api call and compares it against the current time to automatically 
# set your wallpaper based on if its day or night time :) 

# set exact path of wallpapers here 
day_wallpaper = "C:\\Users\\SetYourPathHere"
night_wallpaper = "C:\\Users\\SetYourPathHere"

# returns datetime object with sunset time 
def set_sunset(data, now):
	sunset = data['sunset']

	if (sunset[1] == ':'):
		sunset = "0" + sunset

	sunset_hour = int(sunset[0] + sunset[1]) - 4
	sunset_hour = sunset_hour + 12 # set hour to be in 24 hour format 
	sunset_minute = int(sunset[3] + sunset[4])
	sunset_time = datetime.datetime(now.year, now.month, now.day, sunset_hour, sunset_minute)

	return sunset_time

# returns datetime object with sunrise time 
def set_sunrise(data, now):
	sunrise = data['sunrise']

	if (sunrise[1] == ":"):
		sunrise = "0" + sunrise

	sunrise_hour = int(sunrise[0] + sunrise[1]) - 4
	sunrise_minute = int(sunrise[3] + sunrise[4])
	sunrise_time = datetime.datetime(now.year, now.month, now.day, sunrise_hour, sunrise_minute)

	return sunrise_time

# infinite recursion
def change_wallpaper():

	# get sunrise and sunset times from https://api.sunrise-sunset.org
	api_url = "https://api.sunrise-sunset.org/json?lat=40.7127768&lng=-74.005974"
	response = requests.get(api_url)
	api_json = response.json()
	data = api_json.get("results")

	# get current system time in 24h format / and sunrise + sunset times
	now = datetime.datetime.now()
	sunset_time = set_sunset(data, now)
	sunrise_time = set_sunrise(data, now)

	# set night time wallpaper
	if (now < sunset_time and now > sunrise_time): # it must be day time 

		ctypes.windll.user32.SystemParametersInfoW(20, 0, day_wallpaper, 0)

		while datetime.datetime.now() < sunset_time: # loop until current time > sunset time 
			time.sleep(60)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, night_wallpaper, 0)

		change_wallpaper()

	# set day time wallpaper
	else: # it must be night time 

		ctypes.windll.user32.SystemParametersInfoW(20, 0, night_wallpaper, 0)

		while datetime.datetime.now() < sunrise_time: # loop until current time > sunrise time 
			time.sleep(60)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, day_wallpaper, 0)

		change_wallpaper()

change_wallpaper()