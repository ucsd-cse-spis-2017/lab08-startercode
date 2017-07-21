#!/usr/bin/env python
# Import the relevant libraries
import RPi.GPIO as GPIO
import time

LedPin = 11                                     # pin11
BtnPin = 15                                     # pin connected to button

def setup():
        ''' One time set up configurations'''
        GPIO.setmode(GPIO.BOARD)                # Numbers GPIOs by physical location
        GPIO.setup(LedPin, GPIO.OUT)            # Set LedPin's mode is output
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level (3.3V)

        GPIO.output(LedPin, GPIO.HIGH)          # Set LedPin high (+3.3V) to turn off led

def loop():
        while True:
                # This code repeats forever
                button = GPIO.input(BtnPin)
                print(button)

def destroy():
        GPIO.output(LedPin, GPIO.HIGH)          # led off
        GPIO.cleanup()                          # Release resource

if __name__ == '__main__':                      # Program starts here
        setup()
        try:
                loop()
        except KeyboardInterrupt:               # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()

