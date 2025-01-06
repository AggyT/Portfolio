# File: Turns.py
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
# This program is a module that contains functions that tell the MACRO to
# turn a certain direction after choosing which path to take when it
# encounters a fork in the line
# 
# 
# SETUP: BRICKPI PORTS          GROVEPI PORTS
#        A - Back LEFT          D2 - Right Line Finder
#        B - Front              D3 - *NOT USED*
#        C - Gate Motor         D4 - *NOT USED*
#        D - Back Right         D5 - *NOT USED*
#        1 - Touch 1            D6 - *NOT USED*
#        2 - *NOT USED*         D7 - Left Line Finder
#        3 - *NOT USED*         D8 - *NOT USED*
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



def rightTurn(left, right):
    
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)

    print(left, right)
    time.sleep(.5)
    
    BP.set_motor_power(BP.PORT_A, -70)
    BP.set_motor_power(BP.PORT_D, -20)
    BP.set_motor_power(BP.PORT_B, -50)
    
    time.sleep(.5 + .3* right)
    
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)
    
    return        
        
def leftTurn():
      
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)
    
    time.sleep(.5)
    
    BP.set_motor_power(BP.PORT_A, 20)
    BP.set_motor_power(BP.PORT_D, -70)
    BP.set_motor_power(BP.PORT_B, -50)
    
    time.sleep(.5)
    
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)
    
    return


