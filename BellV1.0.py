
#TODO find port for switch
#TODO set up 
import RPi.GPIO as GPIO
import time
from time import gmtime, strftime


#Setwarnings False
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.IN)

RunSystem="True"

x=0

Morningwarning = ("08:43")
Registration = ("08:45")
Period1 = ("09:00")
Period2 = ("09:50")
Startbreak = ("10:40")
Breakwarning = ("10:57")
Period3 = ("11:00")
Period4 =  ("11:50")
Lunch = ("12:40")
Lunchwarning = ("13:10")
Period5 = ("13:15")
Period6 = ("14:10")
Endofday = ("15:00")

Switch = False
SystemStartTime = strftime("%c")
print("Program started on: ",SystemStartTime)



def GPIOSETUP():
    
    GPIO.setmode(GPIO.BOARD)
    #Pin 12 setup
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(7, GPIO.IN)

def normalBell(a):
    GPIOSETUP()
    while a<3:

        GPIO.output(12, True)
        print("RING")
        time.sleep(1.5)
        GPIO.cleanup()
        print("OFF")
        time.sleep(1.7)
        GPIOSETUP()
        a +=1
    else:
        GPIO.cleanup()
        
def bombBell():
    GPIOSETUP()
    GPIO.output(12, True)
    print("Bomb RING")
    time.sleep(0.5)
    GPIO.cleanup()
    print("OFF")
    time.sleep(0.5)
    GPIOSETUP()

while RunSystem=="True":
    if (GPIO.input(7)):
        bombBell()
    elif strftime("%H:%M") == Morningwarning:
            print("Moringwarning working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Registration:
            print("Registration working")
            normalBell(x)         
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Period1:
            print("Period 1 working")
            normalBell(x)         
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Period2:
            print("Period 2 working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Startbreak:
            print("Startbreak working")
            normalBell(x)       
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Breakwarning:
            print("Breakwarning working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Period3:
            print("Period 3 working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Period4:
            print("Period 4 working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Lunch:
            print("Lunch 1st working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Lunchwarning:
            print("Lunchwarning working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Period5:
            print("Period 5 working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Period6:
            print("Period 6 working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    elif strftime("%H:%M") == Endofday:
            print("End of day working")
            normalBell(x)
            time.sleep(60)
            GPIOSETUP()
    else:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.IN)



GPIO.cleanup()

#bellChoice()



    
