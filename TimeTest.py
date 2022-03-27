import time
from time import gmtime, strftime
from datetime import datetime
now = datetime.now()
SystemStartTime = strftime("%d/%m/%Y at %H:%M:%S")
print("Program started on:",SystemStartTime)

RunSystem="True"
times = ["08:43","08:45","19:17","09:00","09:50","10:40","10:57","11:00","11:50","12:40","13:10","13:15","14:10","15:00"]

while RunSystem=="True":
    if strftime("%H:%M") in times:
        print("Bell rang at",strftime("%H:%M:%S"))
        #normalBell(x)
        time.sleep(60)
        #GPIOSETUP()
