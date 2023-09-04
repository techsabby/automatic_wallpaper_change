import time
import datetime
import functions

# this program gets the sunrise and sunset times for your area 
# via an api call and compares it against the current time to automatically 
# to set your wallpaper based on if its day or night time :) 

while True:
    today_date = str(datetime.date.today())
    api_data = functions.return_apicall(today_date) # returns sunrise and sunset times 
    sunrise_date_time_EST = functions.return_sunrise_date_time_EST(api_data, datetime.date.today()) # extracts sunrise time
    sunset_date_time_EST = functions.return_sunset_date_time_EST(api_data, datetime.date.today()) # extracts sunset time 

    # checks to see if it is after sunset (waits for tomorrow's sunrise if it is) otherwise waits for either today's sunrise or sunset
    if (datetime.datetime.now() > sunset_date_time_EST):
        tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)
        api_data = functions.return_apicall(today_date) # still passing today_date b/c api provides next day info after sunset
        sunrise_date_time_EST = functions.return_sunrise_date_time_EST(api_data, tomorrow_date)

        functions.run_gsettings("set_night_wallpaper")

        while (datetime.datetime.now() < sunrise_date_time_EST):
            time.sleep(60)

        functions.run_gsettings("set_day_wallpaper")

    else:
        if (datetime.datetime.now() < sunrise_date_time_EST):

            functions.run_gsettings("set_night_wallpaper")

            while(datetime.datetime.now() < sunrise_date_time_EST):
                time.sleep(60)

            functions.run_gsettings("set_day_wallpaper")

        else:

            functions.run_gsettings("set_day_wallpaper")

            while(datetime.datetime.now() < sunset_date_time_EST):
                time.sleep(60)

            functions.run_gsettings("set_night_wallpaper")