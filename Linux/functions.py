import os
import requests
import datetime

latitude = "40.712784"
longitude = "-74.005943"

api_url = "https://api.sunrise-sunset.org/json?lat=" + latitude + "&lng=" + longitude + "&date="

gsettings_command = "gsettings set org.gnome.desktop.background picture-uri"
wallpaper_path = "/home/sabby/Pictures/Automatic/"

def return_apicall(date):
    response = requests.get(api_url + date)
    api_json = response.json()
    api_data = api_json.get("results")
    
    return api_data

def return_sunrise_date_time_EST(api_data, date):
	sunrise = api_data['sunrise']

	if (sunrise[1] == ":"):
		sunrise = "0" + sunrise

	sunrise_hour = int(sunrise[0] + sunrise[1]) - 4
	sunrise_minute = int(sunrise[3] + sunrise[4])
	sunrise_date_time_EST = datetime.datetime(date.year, date.month, date.day, sunrise_hour, sunrise_minute)

	return sunrise_date_time_EST

def return_sunset_date_time_EST(api_data, date):
	sunset = api_data['sunset']

	if (sunset[1] == ':'):
		sunset = "0" + sunset

	sunset_hour = int(sunset[0] + sunset[1]) - 4
	sunset_hour = sunset_hour + 12 # set hour to be in 24 hour format 
	sunset_minute = int(sunset[3] + sunset[4])
	sunset_date_time_EST = datetime.datetime(date.year, date.month, date.day, sunset_hour, sunset_minute)

	return sunset_date_time_EST

# changing wallpapers based on system light/dark theme currently not supported (both are run)
def run_gsettings(wallpaper_name):
	os.system(gsettings_command + " //" + wallpaper_path + wallpaper_name)
	os.system(gsettings_command + "-dark //" + wallpaper_path + wallpaper_name)