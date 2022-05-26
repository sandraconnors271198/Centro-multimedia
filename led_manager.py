# !/usr/bin/env python3
# ## ###############################################
#
# led_manager.py
# Controls leds in the GPIO
#
# Autor: Pérez Gutiérrez Sandra
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
import virtualboard


GPIO.setmode(GPIO.BOARD)

GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)


#Casos para encender los LEDS
def leds(num):
        if num == 7:
                GPIO.output(32, GPIO.HIGH) # Turn led           #Led 7
                GPIO.output(24, GPIO.LOW)  # Turn led off
                GPIO.output(22, GPIO.LOW)  # Turn led off
                GPIO.output(18, GPIO.LOW)  # Turn led off
                GPIO.output(16, GPIO.LOW)  # Turn led off
                GPIO.output(12, GPIO.LOW)  # Turn led off
                GPIO.output(10, GPIO.LOW)  # Turn led off
                
        if num == 6:
                GPIO.output(26, GPIO.HIGH) # Turn led        #Led 6
                GPIO.output(26, GPIO.LOW)  # Turn led off
                GPIO.output(22, GPIO.LOW)  # Turn led off
                GPIO.output(18, GPIO.LOW)  # Turn led off
                GPIO.output(16, GPIO.LOW)  # Turn led off
                GPIO.output(12, GPIO.LOW)  # Turn led off
                GPIO.output(10, GPIO.LOW)  # Turn led off

        if num == 5:
                GPIO.output(24, GPIO.HIGH) # Turn led        #Led 5
                GPIO.output(26, GPIO.LOW)  # Turn led off
                GPIO.output(24, GPIO.LOW)  # Turn led off
                GPIO.output(18, GPIO.LOW)  # Turn led off
                GPIO.output(16, GPIO.LOW)  # Turn led off
                GPIO.output(12, GPIO.LOW)  # Turn led off
                GPIO.output(10, GPIO.LOW)  # Turn led off

        if num == 4:
                GPIO.output(22, GPIO.HIGH) # Turn led         #Led 4
                GPIO.output(26, GPIO.LOW)  # Turn led off
                GPIO.output(24, GPIO.LOW)  # Turn led off
                GPIO.output(22, GPIO.LOW)  # Turn led off
                GPIO.output(16, GPIO.LOW)  # Turn led off
                GPIO.output(12, GPIO.LOW)  # Turn led off
                GPIO.output(10, GPIO.LOW)  # Turn led off

        if num == 3:
                GPIO.output(18, GPIO.HIGH) # Turn led     #Led 3
                GPIO.output(26, GPIO.LOW)  # Turn led off
                GPIO.output(24, GPIO.LOW)  # Turn led off
                GPIO.output(22, GPIO.LOW)  # Turn led off
                GPIO.output(18, GPIO.LOW)  # Turn led off
                GPIO.output(12, GPIO.LOW)  # Turn led off
                GPIO.output(10, GPIO.LOW)  # Turn led off

        if num == 2:
                GPIO.output(16, GPIO.HIGH) # Turn led       #Led 2
                GPIO.output(26, GPIO.LOW)  # Turn led off
                GPIO.output(24, GPIO.LOW)  # Turn led off
                GPIO.output(22, GPIO.LOW)  # Turn led off
                GPIO.output(18, GPIO.LOW)  # Turn led off
                GPIO.output(16, GPIO.LOW)  # Turn led off
                GPIO.output(10, GPIO.LOW)  # Turn led off

        if num == 1:
                GPIO.output(12, GPIO.HIGH) # Turn led    #Led 1
                GPIO.output(26, GPIO.LOW)  # Turn led off
                GPIO.output(24, GPIO.LOW)  # Turn led off
                GPIO.output(22, GPIO.LOW)  # Turn led off
                GPIO.output(18, GPIO.LOW)  # Turn led off
                GPIO.output(16, GPIO.LOW)  # Turn led off
                GPIO.output(10, GPIO.LOW)  # Turn led off
        pass



def bcd(num):
		GPIO.output(36,GPIO.HIGH if (num & 0x00000001)  > 0 else GPIO.LOW)   
		GPIO.output(38, GPIO.HIGH if (num & 0x00000002) > 0 else GPIO.LOW)  
		GPIO.output(40, GPIO.HIGH if (num & 0x00000004) > 0 else GPIO.LOW)
		GPIO.output(37, GPIO.HIGH if (num & 0x00000008) > 0 else GPIO.LOW)	
        
        

def marquee(type='pingpong'):
	switcher = {
		'left'     : _marquee_left,
		'right'    : _marquee_right,
		'pingpong' : _marquee_pingpong
	}
	func = switcher.get(type, None)
	if func:
		func()


def _marquee_right():
        GPIO.output(10, GPIO.HIGH)      # Turn led on
        GPIO.output(12, GPIO.HIGH)      # Turn led on  
        sleep(0.1)
        GPIO.output(10, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(12, GPIO.HIGH)      # Turn led on
        GPIO.output(16, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(12, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(16, GPIO.HIGH)      # Turn led on
        GPIO.output(18, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(16, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(18, GPIO.HIGH)      # Turn led on
        GPIO.output(22, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(18, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(22, GPIO.HIGH)      # Turn led on
        GPIO.output(24, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(22, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(24, GPIO.HIGH)      # Turn led on
        GPIO.output(26, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(24, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(26, GPIO.HIGH)      # Turn led on
        GPIO.output(32, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(26, GPIO.LOW)       # Turn led off
        sleep(0.3)
        GPIO.output(32, GPIO.LOW)       # Turn led off
        
def _marquee_left():                                                  
        GPIO.output(32, GPIO.HIGH)      # Turn led on		       
        GPIO.output(26, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(32, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(26, GPIO.HIGH)      # Turn led on
        GPIO.output(24, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(26, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(24, GPIO.HIGH)      # Turn led on
        GPIO.output(22, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(24, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(22, GPIO.HIGH)      # Turn led on
        GPIO.output(18, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(22, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(18, GPIO.HIGH)      # Turn led on
        GPIO.output(16, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(18, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(16, GPIO.HIGH)      # Turn led on
        GPIO.output(12, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(16, GPIO.LOW)       # Turn led off
        sleep(0.1)
        GPIO.output(12, GPIO.HIGH)      # Turn led on
        GPIO.output(10, GPIO.HIGH)      # Turn led on
        sleep(0.1)
        GPIO.output(12, GPIO.LOW)       # Turn led off
        sleep(0.2)
        GPIO.output(10, GPIO.LOW)       # Turn led off


def _marquee_pingpong():  
	_marquee_right()   
	_marquee_left()    
