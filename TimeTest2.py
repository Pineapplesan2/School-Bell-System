import time
from time import gmtime, strftime
from datetime import datetime
file = open(r'N:/BellSystem/BellTimes.txt', 'r+')
timeArray = file.readlines()
timeArray = [x.strip() for x in timeArray]
print(timeArray)
file.close()


RunSystem="True"
while RunSystem=="True":
    if strftime("%H:%M") in timeArray:
        print("Bell rang at",strftime("%H:%M:%S"))
        #normalBell(x)
        time.sleep(60)
        #GPIOSETUP()
    else:
        print("No Bell")
        file = open(r'N:/BellSystem/BellTimes.txt', 'r+')
        timeArray = file.readlines()
        timeArray = [x.strip() for x in timeArray]
        print(timeArray)
        file.close()
        time.sleep(30)
        
