# File: constants.py
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
# This file contains the constants used in the MACRO program
# 
# SETUP: BRICKPI PORTS          GROVEPI PORTS
#        A - Back LEFT          D2 - Right Line Finder
#        B - Front              D3 - *NOT USED*
#        C - Gate Motor         D4 - *NOT USED*
#        D - Back Right         D5 - *NOT USED*
#        1 - *NOT USED*         D6 - *NOT USED*
#        2 - *NOT USED*         D7 - Left Line Finder
#        3 - *NOT USED*         D8 - *NOT USED*
#        4 - TOUCH 1            A0 - *NOT USED*
#                               A1 - *NOT USED*
#                               A2 - *NOT USED*
#
# -----------------------------------------------------------------------
import math

RIGHT = 2 # Right linefinder
LEFT = 7 # Left linefinder
POWER = -60 # Motor power
SLEEP = .01 # Time delay
KP = 40 # Proportional constant
KI = 800000 # Integral constant
KD = 1000000 # Derivative constant
THRESHOLD = 10 # Analog signal threshold from hall sensor
MAGDEAD = 5 # Magnet Deadzone time, does not accept hall input
DIAMETER = 6.0325 # Wheel Diameter
SPEED = 18 # CHANGE THIS TO CHANGE DPS

# Derived Constants
RADIUS = DIAMETER / 2
DPS = SPEED / RADIUS * 180 / math.pi
