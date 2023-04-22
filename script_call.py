import datetime
import time 

target_time = datetime.datetime(2023, 4, 21, 20, 54)

while datetime.datetime.now() < target_time:
	time.sleep(10)
print('Test Successful!')






#now = datetime.datetime.now().strftime("%I")
#print(now)
#test= datetime.datetime.now()
#print(test.minute)
#print(now.hour)
#print(datetime.datetime.now())