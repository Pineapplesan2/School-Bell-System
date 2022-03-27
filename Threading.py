import threading
import RPi.GPIO as GPIO
import os
from time import sleep, strftime

def gpioSetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(15, GPIO.IN)
    GPIO.setup(11, GPIO.OUT)
    gpioSelfTest()

def gpioSelfTest():
    print("""
             #################
               GPIO SELFTEST
             #################""")

    for i in range(2):
        try:
            GPIO.output(11, GPIO.LOW)
            sleep(1)
            GPIO.output(11, GPIO.HIGH)
            sleep(1)

        except RuntimeError:
            print("GPIO SELFTEST FAILED. Please restart the program")
            input("Press enter to exit. ")
            exit()

    print("""
             #################
              SELFTEST PASSED
             #################\n""")
    sleep(4)
    os.system('clear')

def clock():
    #print("Clock Thread Started\n")
    while True:
      currentTime = strftime("%H:%M:%S")
      return currentTime
      sleep(0.5)

def day():
    #print("Day Thread Started\n")
    while True:
      currentDay = strftime("%A")
      return currentDay
      sleep(6000)

def fileUpdater():

    print("File Updater Thread Started")
    while True:
        try:
            times=[]
            timeFile= open("times.bell","r+")
            for time in timeFile.readlines():
                times.append(time)
            timeFile.close()
            #print("fileUpdater Thread Started")
            print("Times Updated")
            #print(times)
            return times
            sleep(20)
        except RuntimeError:
            print("Times failed to load.")
            input("Press enter to try again")
            pass
            


def outputTimes():
   #sleep(20)
    while True:
        print("The current time is", clock())
        sleep(30)


def ring():
    for i in range(1, 10):
        print("ON")
        GPIO.output(11, GPIO.LOW)
        sleep(1)
        print("OFF")
        GPIO.output(11, GPIO.HIGH)
        sleep(1)

def emergencyCheck():
    while True:
        if GPIO.input(15):
            GPIO.output(11, GPIO.LOW)
            print("EMERGENCY")
            sleep(0.5)
            GPIO.output(11, GPIO.HIGH)
            sleep(0.5)
        else:
            GPIO.output(11, GPIO.HIGH)

def system():
    currentTime = clock()
    currentDay = day()
    sleep(10)
    print("The current day is", currentDay)
    print("The current time is", currentTime)
    timeList = fileUpdater()
    print(timeList)
    while True:
        if currentTime in fileUpdater():
            ring()

def startThreads():
    try:
        threading.Thread(target=main).start()
        threading.Thread(target=system).start()
        threading.Thread(target=clock).start()
        threading.Thread(target=day).start()
        threading.Thread(target=fileUpdater).start()
        #threading.Thread(target=outputTimes).start()
        threading.Thread(target=emergencyCheck).start()

    except RuntimeError:
        print("Threads failed to start. Please restart the program")
        input("Press enter to continue")
        exit()

def main():
    print("""
            Bell Control System
             Connor Millington""")
    gpioSetup()

startThreads()
