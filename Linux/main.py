import time
import logging
import datetime

import weather
import functions

logging.basicConfig(filename="log_file.log", encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

# this program gets the sunrise and sunset times for your area 
# via an api call and compares it against the current time to automatically 
# to set your wallpaper based on if its day or night time :) 

day_sunny_wallpaper = "day.jpeg"
day_rainy_wallpaper = "rain.png"
night_wallpaper = "night.png"

while True:
    logging.info("Program started")
    today_date = str(datetime.date.today())
    api_data = functions.return_apicall(today_date) 
    sunrise_date_time_EST = functions.return_sunrise_date_time_EST(api_data, datetime.date.today()) 
    sunset_date_time_EST = functions.return_sunset_date_time_EST(api_data, datetime.date.today()) 

    # checks to see if it is after sunset (waits for tomorrow's sunrise if it is) otherwise waits for either today's sunrise or sunset
    if (datetime.datetime.now() > sunset_date_time_EST):
        logging.info("1")
        tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)
        api_data = functions.return_apicall(today_date) # still passing today_date b/c api provides next day info after sunset
        sunrise_date_time_EST = functions.return_sunrise_date_time_EST(api_data, tomorrow_date)

        functions.run_gsettings(night_wallpaper)

        while (datetime.datetime.now() < sunrise_date_time_EST):
            time.sleep(60)


        if(weather.get_condition() < 1006): 
            functions.run_gsettings(day_sunny_wallpaper)
        else:
            functions.run_gsettings(day_rainy_wallpaper)

        logging.info("2")

    else:
        if (datetime.datetime.now() < sunrise_date_time_EST):
            logging.info("3")
            
            functions.run_gsettings(night_wallpaper)

            while(datetime.datetime.now() < sunrise_date_time_EST):
                time.sleep(60)

            if(weather.get_condition() < 1006): 
                functions.run_gsettings(day_sunny_wallpaper)
            else:
                functions.run_gsettings(day_rainy_wallpaper)

            logging.info("4")

        else:
            logging.info("5")
            
            if(weather.get_condition() < 1006): 
                functions.run_gsettings(day_sunny_wallpaper)
            else:
                functions.run_gsettings(day_rainy_wallpaper)

            while(datetime.datetime.now() < sunset_date_time_EST):
                time.sleep(60)

                if(weather.get_condition() < 1006): 
                    functions.run_gsettings(day_sunny_wallpaper)
                else:
                    functions.run_gsettings(day_rainy_wallpaper)

            functions.run_gsettings(night_wallpaper)

            logging.info("6")