# File: p3_line_finder3_PID.py
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
# This program is a code written for the speed test portion of the
# demonstration.
# 
# SETUP: BRICKPI PORTS          GROVEPI PORTS
#        A - Back LEFT          D2 - Right Line Finder
#        B - Front              D3 - *NOT USED*
#        C - Gate Motor         D4 - *NOT USED*
#        D - Back Right         D5 - *NOT USED*
#        1 - *NOT USED*         D6 - *NOT USED*
#        2 - *NOT USED*         D7 - Left Line Finder
#        3 - *NOT USED*         D8 - *NOT USED*
#        4 - Touch 1            A0 - *NOT USED*
#                               A1 - *NOT USED*
#                               A2 - *NOT USED*
#
# -----------------------------------------------------------------------
import time
import brickpi3
import constants as k


BP = brickpi3.BrickPi3() # make an instance of BP
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.TOUCH)

try:
    
    print("Press touch sensor 1 to begin.")
    value = 0
    while not value:
        try:
            value = BP.get_sensor(BP.PORT_4)
        except brickpi3.SensorError:
            pass

    initialTime = time.time()
    
    BP.set_motor_dps(BP.PORT_A + BP.PORT_D, k.DPS)
    BP.set_motor_dps(BP.PORT_B, -1 * k.DPS)
    BP.set_motor_power(BP.PORT_C, 20)

    while (time.time() - initialTime < 300 / k.SPEED):
        time.sleep(.25)
    
except KeyboardInterrupt:
    BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_C + BP.PORT_D, 0)
    BP.reset_all()

BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_C + BP.PORT_D, 0)
BP.reset_all()
