# Project 2
# File: MISC.py
# Date: 1 September 2014
# By: Natalie Harvey
# harve115
# Matthew Stuber
# mjstuber
# Alyssa Devincenzi 
# adevinc
# Agathiya Tharun
# atharun
# Section: 2
# Team: 30
#
# ELECTRONIC SIGNATURE
# Natalie Harvey
# Matthew Stuber
# Alyssa Devincenzi
# Agathiya Tharun
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# This module contains miscellaneous functions used in the main program.
import math as m
import constants as k

# Velocity of water
def WaterVelocity(flowRate, area):
    return (flowRate / area)
    
# Water Head of Reservoir
def WaterHead(elevation, depth):
    return (elevation + depth / 2)

# Fill/Drain time
def Time(mass, flowRate):
    return (mass / k.density / flowRate / 3600)

def JoulestoMWH(joules):
    return (joules / 3.6 / m.pow(10, 9))

def MWHtoJoules(MWH):
    return (MWH * 3.6 * m.pow(10,9))