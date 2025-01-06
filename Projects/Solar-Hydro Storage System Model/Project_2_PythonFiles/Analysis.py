# Project 2 Analysis
# File: Analysis.py
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
# This program loops through all the possible combinations, analyzing
# each for Ein, Cost, and Cost to Efficiency ratio. It will output the
# results to a txt file in CSV format that allows the user to perfrom
# further analysis such as sorting the data.
from BendLoss import bendloss
import constants as k
from headLoss import headLoss
import inputsAnalysis as i
import MISC
import math
import costFinder as cost
import WallConstructionCosts as wall
#-----------------------------------------------------------------------------
case = 1
filename = "zone {} analysis".format(str(i.zone))
out = open("./" + filename + ".txt", "w")
out.write("Zone = {},Elevation = {},Length = ".format(i.zone, i.hWater))
for length in i.lPipe:
    out.write("-{}".format(length))
out.write(",Bends = ")
for b in i.bendCoefficient:
    out.write("-{}".format(b))
out.write(",\n")
out.write("Case,Pump Efficiency, Pump Flow Rate, Pipe Diameter, Pipe friction Coefficient, Turbine Efficiency, Turbine Flow Rate, Total Pipes, Depth, Ein, Cost, $ / %Efficiency\n")

def analyze(case, zone, nPump, QPump, dPipe, lPipe, fPipe, tPipes, nPipes, depth, head, bend, nTurbine, QTurbine):

    bendLossDown = 0
    frictionLossDown = 0
    bendLossUp = 0
    frictionLossUp = 0
    
    # Intermediate Calculations
    pipeAreaUp = math.pi * ((dPipe / 2) ** 2)
    pipeAreaDown = math.pi * ((dPipe / 2) ** 2)
    velocityUp = MISC.WaterVelocity(QPump, pipeAreaUp)
    velocityDown = MISC.WaterVelocity(QTurbine, pipeAreaDown)
    waterHead = MISC.WaterHead(head + dPipe, depth - dPipe)
    
    for length in lPipe:
        frictionLossDown += headLoss(dPipe, fPipe, length, velocityDown) 
    
    for b in bend:
        bendLossDown += bendloss(velocityDown, b)
    
    for length in lPipe:
        frictionLossUp += headLoss(dPipe, fPipe, length, velocityUp) 
    
    for b in bend:
        bendLossUp += bendloss(velocityUp, b)
    
    #Key Intermediate Calculation
    Mass = k.Eout * (1 / nTurbine)
    Mass = Mass / (k.g * waterHead - (tPipes - nPipes) * (frictionLossDown + bendLossDown))
    
    #Other Main Calculations
    area = (Mass / k.density) / (depth - dPipe)
    fillTime = MISC.Time(Mass, QPump)
    drainTime = MISC.Time(Mass, QTurbine)
    Ein = Mass / nPump
    Ein = Ein * (k.g * waterHead + (tPipes - nPipes) * (bendLossUp + frictionLossUp))
    Ein = MISC.JoulestoMWH(Ein)
    efficiency = MISC.JoulestoMWH(k.Eout) / Ein
        
    if (area < 0 or area > wall.zoneDict[str(zone)][3] or fillTime > 5 or drainTime > 12 or efficiency < .6):
        return
    
    tCost = cost.findCost(zone, nPump, QPump, dPipe, lPipe, fPipe, tPipes, depth, head, area, bend, nTurbine, QTurbine, i.areaUnderPipes)
    unitCost = tCost / (100 * efficiency)
    
    out.write("{},{},{},{},{},{},{},{},{},{},{},{}\n".format(case,nPump, QPump, dPipe, fPipe, nTurbine, QTurbine, tPipes, depth, Ein, tCost, unitCost))
    return

#analyze(1, .89,25,2,[115.47],.01,1,0,16,100,[.22,.22],.92,11)
for nP in i.nPump:
    for QP in i.Qpump:
        for diameter in i.dPipe:
            for friction in i.fPipe:
                for depth in i.dWater:
                    for nT in i.nTurbine:
                        for QT in i.Qturbine:
                            for x in range(0,len(i.totalPipes)):
                                analyze(case, i.zone, nP, QP, diameter, i.lPipe, friction, i.totalPipes[x], i.nPipe[x], depth, i.hWater, i.bendCoefficient, nT, QT)
                                case += 1
out.close()
print("\aDone!")