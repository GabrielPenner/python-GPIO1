#!/usr/bin/env python

# Import os, sys, and GPIO modules and specific sleep function from time
import os
import sys
from time import sleep
import RPi.GPIO as GPIO

'''
Set to use Broadcom GPIO pin numbering and assigning pin functions.
Buttons take input while the LEDs receive output.
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
#GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

# Defining blink function to flash LED every .3 seconds for .3 seconds
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        sleep(0.3)
        GPIO.output(pin,GPIO.LOW)
        sleep(0.3)

'''
I took .wav files from MicroSoft's old 3D pinball game.
This loop calls one of the .wav files and blinks the 2 LEDs 5 times while the sound runs (about 5 seconds).
Testing the sys.exit and GPIO.cleanup functions in the first if statement.
'''
while True:
        if (GPIO.input(25) == False):
                os.system('aplay shipstart.WAV &')
                for i in range(0,5):
                        blink(17)
                        blink(22)
                GPIO.cleanup()
                sys.exit()

# Commented out for later use.
#       if (GPIO.input(22) == False):
#               os.system('aplay laser.WAV &')

# Only runs the sound file. Does not blink the LEDs.
        if (GPIO.input(23) == False):
                os.system('aplay ship3.WAV &')

# This keeps one button press from running the loop multiple times.
        sleep(0.25);
