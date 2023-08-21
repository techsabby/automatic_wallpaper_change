import os
import time
import requests
import datetime

# this program gets the sunrise and sunset times for your area 
# via an api call and compares it against the current time to automatically 
# set your wallpaper based on if its day or night time :) 

latitude = ""
longitude = ""

# url for api call 
api_url = "https://api.sunrise-sunset.org/json?lat=" + latitude + "&lng=" + longitude + "&date="

# --------------------------- help functions --------------------------- #
def return_apicall(date):
	response = requests.get(api_url + date)
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

# --------------------------- main function  --------------------------- #
def change_wallpaper():
	today_date = str(datetime.date.today())
	data = return_apicall(today_date)
	sunrise_time = return_sunrise(data, datetime.date.today())
	sunset_time = return_sunset(data, datetime.date.today())

	# checks to see if the time is after sunset then waits for tommorow's sunrise
	if (datetime.datetime.now() > sunset_time):
		tmmr_date = str(datetime.date.today() + datetime.timedelta(days=1))
		data = return_apicall(today_date)
		sunrise_time = return_sunrise(data, datetime.date.today() + datetime.timedelta(days=1))

		while (datetime.datetime.now() < sunrise_time):
			time.sleep(60)

		os.system("gsettings set org.gnome.desktop.background picture-uri file:///path/to/night/wallpaper")
		os.system("gsettings set org.gnome.desktop.background picture-uri-dark file:///path/to/night/wallpaper")

		change_wallpaper()

	# otherwise checks to see if it's before sunrise today then waits for either sunrise or sunset today 
	else:
		if (datetime.datetime.now() < sunrise_time):
			while(datetime.datetime.now() < sunrise_time):
				time.sleep(60)

			os.system("gsettings set org.gnome.desktop.background picture-uri file:///path/to/day/wallpaper")
			os.system("gsettings set org.gnome.desktop.background picture-uri-dark file:///path/to/day/wallpaper")
			
			change_wallpaper()

		else:
			while(datetime.datetime.now() < sunset_time):
				time.sleep(60)

			os.system("gsettings set org.gnome.desktop.background picture-uri file:///path/to/day/wallpaper")
			os.system("gsettings set org.gnome.desktop.background picture-uri-dark file:///path/to/day/wallpaper")
			
			change_wallpaper()

change_wallpaper()