# File: calibration.py
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
# This program calibrates the IMU
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
from MPU9250 import MPU9250
import numpy as np
import sys
import smbus
import time

from IMUFilters import AvgCali
from IMUFilters import KalmanFilter
from IMUFilters import FindSTD
from IMUFilters import InvGaussFilter

# NOTE: This is sample code that reads acceleration, gyro, and magnetic data
# from the GrovePi IMU, filters it based on user parameters, and writes it to
# a CSV file.

def calibrateIMU():
    mpu9250 = MPU9250()
        
    #Parameters
    depth=100
    dly=0.01
    adv = True
    #/////////
    
    # [r,q]Will need to play with each filter value
    # 
    # A note on Kalman filter parameters: Each of these parameters represents the process and system noise respectively.
    # In order to adjust the output of the Kalman filter, each of these parameters can be modified.  Do not set these
    # parameters to zero, because a Kalman filter actually needs a little bit of noise, or it becomes unstable and 
    # effectively useless.
    
    # System Noise:  Setting the system noise to a high value will make the filter less responsive to subtle changes in
    # the environment.  Practically speaking, if you tell your filter that the system is going to be very noisy, it will
    # likely assume small changes are just noise.  Telling your filter that the system will have a low amount of noise
    # will make it more "aggressive".
    
    # Process Noise:  Process noise is a "natural noise" that grows over time proportional to how often you are making 
    # measurements.  What it attempts to model is the fact that the states change between measurements, so there is an
    # additional uncertainty on top of any noise in the sensors.  There are advanced methods for calculating good estimates
    # process noise, but generally for this course, guessing and testing should be a decent method.
    
    # Calibration and Filter Setup
    
    biases=AvgCali(mpu9250,depth,dly)
    state=[[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0,0,0,0,0,0,0,0,0]]#Estimated error (p) and measurement state (x) 
    std=FindSTD(biases,mpu9250,dly)
    count = 3 #Number of standard deviations used for filtering
    
    magCals = [adv, state[1][7], biases[7], std[7], count]
    
    return magCals

def readMag(magCals):
    mpu9250 = MPU9250()
    dly=0.01
    flter=[[0.7,1.0],[0.7,1.0],[0.7,1.0],[0.7,1.0],[0.7,1.0],[0.7,1.0],[5,2],[5,2],[5,2]]
    state=[[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0,0,0,0,0,0,0,0,0]]
    state=KalmanFilter(mpu9250,state,flter,dly)
    
    return InvGaussFilter(magCals[0], state[1][7], magCals[2], magCals[3], magCals[4])
