# Project 2 Inputs for Analysis
# File: inputsAnalysis.py
# Date: December 6 2020
# By: Matthew Stuber
# mjstuber
# Natalie Harvey
# harve115
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
# This program contains the input values for the analysis program

#BEGIN
zone            = 3                                             # Zone choice
nPump           = [0.89, .92]                                   # Pump efficiency
Qpump           = [x for x in range(25, 51, 1)]                 # Pump flow volume (m^3/s)
dPipe           = [float(d/100) for d in range(75, 325, 25)]    # Pipe diameter (m) 
lPipe           = [43.84412423,70.71380809]                     # Pipe length (m)
fPipe           = [.05,.03,.02,.01,.005,.002]                   # Pipe friction coefficient 
dWater          = [d for d in range(5, 21)]                     # Depth of water reservoir (m)
hWater          = 65                                            # Elevation of water reservoir (m)
bendCoefficient = [.1, .1, .2, .2]                              # Pipe bend coefficient
nTurbine        = [0.89, .92, .94]                              # Turbine efficiency
Qturbine        = [x for x in range(10, 40, 1)]                 # Turbine flow volume (m^3/s)
totalPipes      = [1,2,4,6]                                     # total number of pipes (up & down)
nPipe           = [0,1,2,3]                                     # number of pipes in one direction (0 if 1 total pipe)
areaUnderPipes  = 0                                             # area below raised pipe instalation (user defined)