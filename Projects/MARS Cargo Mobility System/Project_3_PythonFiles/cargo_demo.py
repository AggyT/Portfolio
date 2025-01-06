# File: cargo_demo.py
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
# This program is to demonstrate the cargo drop off capabilities. 
# 
# 
# SETUP: BRICKPI PORTS          GROVEPI PORTS
#        A - Back LEFT          D2 - Right Line Finder
#        B - Front              D3 - *NOT USED*
#        C - Gate Motor         D4 - *NOT USED*
#        D - Back Right         D5 - *NOT USED*
#        1 - *NOT USED*         D6 - *NOT USED*
#        2 - *NOT USED*         D7 - Left Line Finder
#        3 - *NOT USED*         D8 - *NOT USED*
#        4 - *NOT USED*         A0 - *NOT USED*
#                               A1 - *NOT USED*
#                               A2 - *NOT USED*
#
# -----------------------------------------------------------------------
import time
import brickpi3
import grovepi
import math
import constants as k
import iop3
import imu
import Turns
import Drop


BP = brickpi3.BrickPi3() # make an instance of BP
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.TOUCH)

magCals = imu.calibrateIMU()

grovepi.pinMode(k.LEFT, "INPUT")
grovepi.pinMode(k.RIGHT, "INPUT")
magnet = time.time()

try:
    print("Press touch sensor 1 to begin.")
    value = 0
    while not value:
        try:
            value = BP.get_sensor(BP.PORT_4)
        except brickpi3.SensorError:
            pass
    
    BP.set_motor_power(BP.PORT_C, 20)
    BP.set_motor_power(BP.PORT_B, -1 * k.POWER)
      
    
    while True:
        try: # read in line finder values
            left = grovepi.digitalRead(k.LEFT)
            right = grovepi.digitalRead(k.RIGHT)
            magnet = abs(imu.readMag(magCals))
            
            
        except IOError:
            pass
        
        if (magnet > k.THRESHOLD):# and time.time() - magTime > k.MAGDEAD):
            iop3.cargoDropInit()
            Drop.dropOff()
            iop3.cargoDropFin()
            break
                       
        if (left == 1 and right == 1):
            while (grovepi.digitalRead(k.RIGHT) == 1): 
                BP.set_motor_power(BP.PORT_D, k.POWER)
                time.sleep(k.SLEEP)
            
        elif (left == 1):
            while (grovepi.digitalRead(k.RIGHT) == 0):
                BP.set_motor_power(BP.PORT_A, 0 * k.POWER)
                BP.set_motor_power(BP.PORT_D, k.POWER)
                time.sleep(k.SLEEP)

            BP.set_motor_power(BP.PORT_A + BP.PORT_D, 0)
                
        elif (right == 1):
            while (grovepi.digitalRead(k.LEFT) == 0):
                BP.set_motor_power(BP.PORT_A, k.POWER)
                BP.set_motor_power(BP.PORT_D, 0 * k.POWER)
                time.sleep(k.SLEEP)

            BP.set_motor_power(BP.PORT_A + BP.PORT_D, 0)

        else:  
            while (grovepi.digitalRead(k.RIGHT) == 0):
                BP.set_motor_power(BP.PORT_A, 0 * k.POWER)
                BP.set_motor_power(BP.PORT_D, k.POWER)
                time.sleep(k.SLEEP)

            BP.set_motor_power(BP.PORT_A + BP.PORT_D, 0)
                
except KeyboardInterrupt:
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)
    BP.reset_all()
    
BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_C + BP.PORT_D, 0)
BP.reset_all()