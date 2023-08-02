import json
import time
import requests
import datetime
import ctypes

# this program gets the sunrise and sunset times for your area 
# via an api call and compares it against the current time to automatically 
# set your wallpaper based on if its day or night time :) 

latitude = "set your latitude here"
longitude = "set your longitude here"

# url for api call 
url = "https://api.sunrise-sunset.org/json?lat=" + latitude + "&lng=" + longitude + "&date="

# set exact path of wallpapers here 
day_wallpaper = "C:\\Users\\SetYourPathHere"
night_wallpaper = "C:\\Users\\SetYourPathHere"

# --------------------------- help functions ---------------------------
def return_apicall(date):
	api_url = url + date
	response = requests.get(api_url)
	api_json = response.json()
	data = api_json.get("results")

	return data

def return_sunset(data, date):
	sunset = data['sunset']

	if (sunset[1] == ':'):
		sunset = "0" + sunset

	sunset_hour = int(sunset[0] + sunset[1]) - 4
	sunset_hour = sunset_hour + 12 # set hour to be in 24 hour format 
	sunset_minute = int(sunset[3] + sunset[4])
	sunset_time = datetime.datetime(date.year, date.month, date.day, sunset_hour, sunset_minute)

	return sunset_time

def return_sunrise(data, date):
	sunrise = data['sunrise']

	if (sunrise[1] == ":"):
		sunrise = "0" + sunrise

	sunrise_hour = int(sunrise[0] + sunrise[1]) - 4
	sunrise_minute = int(sunrise[3] + sunrise[4])
	sunrise_time = datetime.datetime(date.year, date.month, date.day, sunrise_hour, sunrise_minute)

	return sunrise_time

# --------------------------- main functions ---------------------------
def change_wallpaper():
	today_date = str(datetime.date.today())
	data = return_apicall(today_date)
	sunset_time = return_sunset(data, datetime.date.today())
	sunrise_time = return_sunrise(data, datetime.date.today())

	# checks to see if the time is after sunset then waits for tommorow's sunrise 
	if (datetime.datetime.now() > sunset_time):
		tmmr_date = str(datetime.date.today() + datetime.timedelta(days=1))
		data = return_apicall(tmmr_date)
		sunrise_time = return_sunrise(data, datetime.date.today() + datetime.timedelta(days=1))

		while (datetime.datetime.now() < sunrise_time):
			time.sleep(60)

		ctypes.windll.user32.SystemParametersInfoW(20, 0, night_wallpaper, 0)

		change_wallpaper()

	# otherwise checks to see if it's before sunrise today then waits for either sunrise or sunset today 
	else:
		if (datetime.datetime.now() < sunrise_time):
			while(datetime.datetime.now() < sunrise_time):
				time.sleep(60)

			ctypes.windll.user32.SystemParametersInfoW(20, 0, day_wallpaper, 0)

			change_wallpaper()

		else:
			while(datetime.datetime.now() < sunset_time):
				time.sleep(60)

			ctypes.windll.user32.SystemParametersInfoW(20, 0, night_wallpaper, 0)

			change_wallpaper()

change_wallpaper()