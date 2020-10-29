import RPi.GPIO as GPIO
import time
import os
import sys

lamo = 3
lamo1 = 4
lamo2 = 2
lamo3 = 17
#pinlist = [lamo]
while True:
    oop = input("Enter input: ")
    if oop =="fan":
        print("on")
        GPIO.setmode(GPIO.BCM)
        pinlist = [lamo]
        GPIO.setwarnings(False)
        GPIO.setup(pinlist, GPIO.OUT)
        GPIO.output(lamo, GPIO.LOW)
#        os.system("clear")
        print("Fan is on ")
    elif oop =="light":
        GPIO.setmode(GPIO.BCM)
        pinlist = [lamo1]
        GPIO.setwarnings(False)
        GPIO.setup(pinlist, GPIO.OUT)
        GPIO.output(lamo1, GPIO.LOW)
#       os.system("clear")
        print("light is on")
    elif oop =="all_off":
        GPIO.setmode(GPIO.BCM)
        pinlist = [lamo, lamo1, lamo2, lamo3]
        GPIO.setwarnings(False)
        GPIO.setup(pinlist, GPIO.OUT)
        GPIO.output(pinlist, GPIO.HIGH)
#      os.system("clear")
        print("every thing is off")
    elif oop =="fan_off":
        GPIO.setmode(GPIO.BCM)
        pinlist = [lamo]
        GPIO.setwarnings(False)
        GPIO.setup(pinlist, GPIO.OUT)
        GPIO.output(pinlist, GPIO.HIGH)
#        os.system("clear")
        print("fan is off")
    elif oop =="light_off":
        GPIO.setmode(GPIO.BCM)
        pinlist = [lamo1]
        GPIO.setwarnings(False)
        GPIO.setup(pinlist, GPIO.OUT)
        GPIO.output(pinlist, GPIO.HIGH)
#        os.system("clear")
        print("light is off")
    elif oop =="exit":
        print("ok bye")
        exit()
    elif oop =="help":
        print("")
        print("light")
        print("light_off")
        print("fan")
        print("fan_off")
        print("all_off")
        print("all_on")
        print("exit")
        print("")
    elif oop =="all_on":
        GPIO.setmode(GPIO.BCM)
        pinlist = [lamo, lamo1, lamo2, lamo3]
        GPIO.setwarnings(False)
        GPIO.setup(pinlist, GPIO.OUT)
        GPIO.output(pinlist, GPIO.LOW)
#        os.system("clear")
        print("all on")
    elif oop =="onebyone":
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(lamo, GPIO.OUT)
#        os.system("clear")
        print("1 relay on")
        time.sleep(1)
        GPIO.output(lamo, GPIO.LOW)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(lamo1, GPIO.OUT)
        print("2 relay on")
        time.sleep(1)
        GPIO.output(lamo1, GPIO.LOW)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(lamo2, GPIO.OUT)
        print("3 relay on")
        time.sleep(0)
        GPIO.output(lamo2, GPIO.LOW)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(lamo3, GPIO.OUT)
        print("4 relay on")
        time.sleep(1)
        GPIO.output(lamo3, GPIO.LOW)
    elif oop =="wave":
        while True:

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(2, GPIO.OUT)
            GPIO.output(2, GPIO.LOW)
            time.sleep(0.1)
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(2, GPIO.OUT)
            GPIO.output(2, GPIO.HIGH)

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(3, GPIO.OUT)
            GPIO.output(3, GPIO.LOW)
            time.sleep(0.1)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(3, GPIO.OUT)
            GPIO.output(3, GPIO.HIGH)

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(4, GPIO.OUT)
            GPIO.output(4, GPIO.LOW)
            time.sleep(0.1)
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(4, GPIO.OUT)
            GPIO.output(4, GPIO.HIGH)

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.LOW)
            time.sleep(0.1)
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.HIGH)


    else:
        print("wrong input "+ oop)
