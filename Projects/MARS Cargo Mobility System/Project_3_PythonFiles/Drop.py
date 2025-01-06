# File: Drop.py
# Date: November 16 2020
# By: Matthew Stuber
# mjstuber
# Section: 2
# Team: 30
# 
# ELECTRONIC SIGNATURE
# Matthew Stuber
# 
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
# 
# This program is a module that contains functions associated with dropping
# the cargo.
# 
# 
# SETUP: BRICKPI PORTS          GROVEPI PORTS
#        A - Back LEFT          D2 - Right Line Finder
#        B - Front              D3 - *NOT USED*
#        C - Gate Motor         D4 - *NOT USED*
#        D - Back Right         D5 - *NOT USED*
#        1 - Touch 1            D6 - *NOT USED*
#        2 - *NOT USED*         D7 - Left Line Finder
#        3 - Analog Hall Sensor D8 - *NOT USED*
#        4 - TOUCH 1            A0 - *NOT USED*
#                               A1 - *NOT USED*
#                               A2 - *NOT USED*
#
# -----------------------------------------------------------------------
import time
import brickpi3
import grovepi
import constants as k

BP = brickpi3.BrickPi3() # make an instance of BP
grovepi.pinMode(k.LEFT, "INPUT")
grovepi.pinMode(k.RIGHT, "INPUT")

def gateDown():
    BP.set_motor_power(BP.PORT_C, -20)
    time.sleep(.75)
    BP.set_motor_power(BP.PORT_C, 0)
    return

def gateUP():
    BP.set_motor_power(BP.PORT_C, 30)
    return

def jerk():
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, -80)
    time.sleep(.5)
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)
    time.sleep(.25)
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, k.POWER)
    return

def dropOff():
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, k.POWER)
    time.sleep(.5)
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)
    gateDown()
    jerk()
    time.sleep(.25)
    gateUP()
    time.sleep(1.25)
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)
    return

