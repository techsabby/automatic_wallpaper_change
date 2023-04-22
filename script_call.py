import datetime
import time 
import ctypes

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)




"""

minute = 44

# (Year, Month, Day, Hour, Minute)
target_time = datetime.datetime(2023, 4, 22, 14, minute)

while datetime.datetime.now() < target_time:
	print('Waiting: ' + str(datetime.datetime.now()))
	time.sleep(10)

print('Test Successful!')
ctypes.windll.user32.SystemParametersInfoW(20, 0, "W:\\Backup\\Documents\\Wallpapers\\f250353280.jpg" , 0)

"""





#now = datetime.datetime.now().strftime("%I")
#print(now)
#test= datetime.datetime.now()
#print(test.minute)
#print(now.hour)
#print(datetime.datetime.now())