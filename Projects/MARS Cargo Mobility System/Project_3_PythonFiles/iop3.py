# File: io.py
# Date: November 13 2020
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
# This file contains the functions associated with user input.
# 
# SETUP: BRICKPI PORTS          GROVEPI PORTS
#        A - Back LEFT          D2 - Right Line Finder
#        B - Front              D3 - *NOT USED*
#        C - Gate Motor         D4 - *NOT USED*
#        D - Back Right         D5 - *NOT USED*
#        1 - *NOT USED*         D6 - *NOT USED*
#        2 - *NOT USED*         D7 - Left Line Finder
#        3 - Analog Hall Sensor D8 - *NOT USED*
#        4 - TOUCH 1            A0 - *NOT USED*
#                               A1 - *NOT USED*
#                               A2 - *NOT USED*
#
# -----------------------------------------------------------------------
import time

def Input():
    while True:
        site = int(input("Enter landing site: 1, 2, 3, or -1 to terminate. -> "))
        if (site == 1 or site == 2 or site ==3):
            validation = input("Confirm site " + str(site) + ". (y/n): ").rstrip().upper()
            if (validation == "Y"):
                return site
            else:
                print("Mission aborted!")
        elif (site == -1):
            validation = input("Confirm shut down. (y/n): ").rstrip().upper()
            if (validation == "Y"):
                return site
            else:
                print("Shut down aborted!")
        else:
            print("Error! Invalid site!")
            
def success():
    print("Run Complete!\n")
    return
    
def startSequence():
    print("Starting in...\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    time.sleep(1)
    return

def siteArrival(site):
    print("Turning off to site " + str(site) + ".")
    return

def cargoDropInit():
    print("Beginning cargo drop off sequence.")
    return

def cargoDropFin():
    print("Cargo drop off complete, heading back to landing site.")
    return