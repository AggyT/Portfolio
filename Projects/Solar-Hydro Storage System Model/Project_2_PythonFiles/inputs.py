# Project 2 Inputs
# File: inputs.py
# Date: December 6 2020
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
# This module contains the input values for the main program

filename = "Output" # name of the output file

#BEGIN
zone            = 1              # Zone choice
nPump           = 0.92           # Pump efficiency
Qpump           = 70            # Pump flow volume (m^3/s)
dPipe           = 2.75              # Pipe diameter (m) 
lPipe           = [67.08203932]  # Pipe length (m) (list form)
fPipe           = 0.002          # Pipe friction coefficient 
dWater          = 13              # Depth of water reservoir (m)
hWater          = 30             # Elevation of water reservoir (m)
bendCoefficient = [0.15, 0.15]   # Pipe bend coefficient (list form)
nTurbine        = 0.94           # Turbine efficiency
Qturbine        = 29            # Turbine flow volume (m^3/s)
totalPipes      = 1              # total number of pipes (up & down)
nPipe           = 0              # number of pipes in one direction (0 if 1 total pipe)
areaUnderPipes  = 0              # area below raised pipe instalation (user defined)   