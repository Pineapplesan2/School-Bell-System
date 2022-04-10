#KEVI Bell System Version 2.1, Created 26/03/2022 by Cameron Mattocks. Creative inspiration for project drawn from KEVI Bell System Version 1.0 by Connor Millington, Cerys Lock and Cameron Mattocks.
from time import strftime
import RPi.GPIO as GPIO
from tkinter import *
import time

#Sets up the Raspberry Pi for use with the bell system, noting which pins to use for I/O.
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.IN)

RunSystem=True
x = 0
print("Program started on:",strftime("%d/%m/%Y at %H:%M:%S")) #Outputs the date and time the program was first started.

def GPIOSETUP(): 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT) #Sets up the pin going into the bell
    GPIO.setup(7, GPIO.IN) #Sets up the pin for the button awaiting input for the bomb bell

def normalBell(a): #A bell will take no longer than 2 multiplied by the amount of seconds there are items in the bell list, so if there are 14 different times the bell goes off, it will take no longer than 28 seconds once a correct time is reached for the bell to ring. This is not to say it WILL take that long, but it is a possibility.
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
    print("Bomb bell ringing on",strftime("%d/%m/%Y at %H:%M:%S"))
    time.sleep(0.5)
    GPIO.cleanup()
    print("OFF")
    time.sleep(0.5)
    GPIOSETUP()

def debugWindow(): #Creates the debug window
    print("Debug menu accessed on:",strftime("%d/%m/%Y at %H:%M:%S"))
    root = Tk()
    root.configure(bg='#254477') #changes background colour of window (Default KEVI Blue)
    root.geometry('200x110') #changes size of window
    myButton1 = Button(root, text="Manually Ring Normal Bell", command=lambda:normalBell(x)).pack() #lambda required in order to pass variable
    myButton2 = Button(root, text="Manually Ring Bomb Bell", command=bombBell).pack()
    myButton3 = Button(root, text="Manually Setup GPIO", command=GPIOSETUP).pack()
    myButton4 = Button(root, text="Resume Program", command=root.destroy).pack()
    root.mainloop()
    
while RunSystem==True:
    file = open(r'/home/pi/Desktop/BellTimes.txt', 'r+') #For a new time to be added into the file, it will take the program 1 second for every different time in the file, so if you have 13 different times that the bell goes off in the file, it will take a max of 13 seconds for a new time to be loaded into the program.
    timeArray = file.readlines() #Reads the file and puts it as one value into a variable
    timeArray = [g.strip() for g in timeArray] #strips the array of any new lines and puts each value into an array ["time and name"]
    file.close() #closes the file to save memory leakage
    for line in timeArray: #for every time in the file
        timeArray = line.split(" ") #split the value into a 2D array so the values become ["time" and "name"]
        if (GPIO.input(7)): #if the bomb bell button is pressed
            bombBell()
        elif timeArray[0] == "debug" and timeArray[-1] == "menu": #if "debug menu" is found in the bell times file
            debugWindow()
            GPIOSETUP()
        elif strftime("%H:%M") in timeArray[0]: #if the current system time matches the first value in the current iteration of timeArray
            print("Bell rang on",strftime("%d/%m/%Y at %H:%M:%S"),"for",timeArray[-1]) #user friendly output with bell ring and the name of the bell that rang
            normalBell(x)
            time.sleep(51) #Cooldown for the remainder of the minute so the bell doesn't ring multiple times in the same instance. (Bell takes 10 seconds to ring, plus an extra second just to be safe.)
            GPIOSETUP()
        else:
            GPIO.cleanup()
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.IN)
            time.sleep(1) #The period between each iteration of the times list. Default=1 (second) to help with RAM and CPU usage, however it means that you are capped at a maximum of 30 different bell times in the file, otherwise you risk bells being skipped completely as it may take up to double the amount of time to execute as there are times in the list.

GPIO.cleanup()
