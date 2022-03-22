#KEVI Bell System Version 2.0, Created 22/03/2022 by Cameron Mattocks. Creative inspiration for project drawn from KEVI Bell System Version 1.0 by Connor Millington, Cerys Lock and Cameron Mattocks.
from time import gmtime, strftime
from datetime import datetime
import RPi.GPIO as GPIO
import time

#Sets up the Raspberry Pi for use with the bell system, noting which pins to use for I/O.
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.IN)

RunSystem="True"
x = 0
Switch = False
SystemStartTime = strftime("%d/%m/%Y at %H:%M:%S")
print("Program started on:",SystemStartTime) #Outputs the date and time the program was first started.

def GPIOSETUP(): 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT) #Sets up the pin going into the bell
    GPIO.setup(7, GPIO.IN) #Sets up the pin for the button awaiting input for the bomb bell

def normalBell(a): #A bell will take no longer than 2 times the amount of seconds there are items in the bell list, so if there are 14 different times the bell goes off, it will take no longer than 28 seconds once a correct time is reached for the bell to ring. This is not to say it WILL take that long, but it is a possibility.
    GPIOSETUP()
    while a<3:
        GPIO.output(12, True)
        print("Ring",a+1)
        time.sleep(1.5)
        GPIO.cleanup()
        print("OFF")
        time.sleep(1.7)
        GPIOSETUP()
        a +=1
    else:
        GPIO.cleanup()
        print("Complete")

def bombBell(): #As long as the bomb bell button is pressed, this function will continue endlessly.
    GPIOSETUP()
    GPIO.output(12, True)
    print("Bomb bell RINGING")
    time.sleep(0.5)
    GPIO.cleanup()
    print("OFF")
    time.sleep(0.5)
    GPIOSETUP()

while RunSystem=="True":
    file = open(r'/home/pi/Desktop/BellTimes.txt', 'r+') #For a new time to be added into the file, it will take the program 1 second for every different time in the file, so if you have 13 different times that the bell goes off in the file, it will take a max of 13 seconds for a new time to be loaded into the program.
    timeArray = file.readlines()
    timeArray = [g.strip() for g in timeArray]
    file.close()
    for line in timeArray:
        timeArray = line.split(" ")
        if (GPIO.input(7)):
            bombBell()
        elif strftime("%H:%M") in timeArray[0]:
            print("Bell rang at",strftime("%H:%M:%S"),"for",timeArray[-1])
            normalBell(x)
            time.sleep(60) #1 minute cooldown so the bell doesn't ring multiple times in the same instance.
            GPIOSETUP()
        else:
            GPIO.cleanup()
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.IN)
            time.sleep(1) #The period between each iteration of the times list. Default=1 (second) to help with RAM and CPU usage, however it means that you are capped at a maximum of 30 different bell times in the file, otherwise you risk bells being skipped completely as it may take up to double the amount of time to execute as there are times in the list.

GPIO.cleanup() 
