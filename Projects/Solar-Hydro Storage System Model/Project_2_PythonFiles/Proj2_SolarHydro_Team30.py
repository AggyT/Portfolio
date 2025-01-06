# Project 2 Main Program
# File: Proj2_SolarHydro_Team30.py
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
# This program uses the inputs from inputs.py to calculate
# the efficiency of the system and the cost of the system.
# It will append the results to a data file specified in inputs.py
#------------------------------------------------------------
from BendLoss import bendloss
import constants as k
from headLoss import headLoss
import inputs as i
import MISC
import math
import costFinder as cost
import time
#---------------------------------------------------------------------------------
bendLossDown = 0         # Head loss from bends in the pipe going down
frictionLossDown = 0     # Head loss from friction in the pipe going down
bendLossUp = 0           # Head loss from bends in the pipe going up
frictionLossUp = 0       # Head loss from friction in the pipe going up
output = []              # Output results to text file

# Intermediate Calculations
pipeAreaUp = math.pi * ((i.dPipe / 2) ** 2)
pipeAreaDown = math.pi * ((i.dPipe / 2) ** 2)
velocityUp = MISC.WaterVelocity(i.Qpump, pipeAreaUp)
velocityDown = MISC.WaterVelocity(i.Qturbine, pipeAreaDown)
waterHead = MISC.WaterHead(i.hWater + i.dPipe, i.dWater - i.dPipe)

# Finding summation of head loss from pipe friction and pipe bends
for length in i.lPipe:
    frictionLossDown += headLoss(i.dPipe, i.fPipe, length, velocityDown) 

for bend in i.bendCoefficient:
    bendLossDown += bendloss(velocityDown, bend)

for length in i.lPipe:
    frictionLossUp += headLoss(i.dPipe, i.fPipe, length, velocityUp) 

for bend in i.bendCoefficient:
    bendLossUp += bendloss(velocityUp, bend)

#Key Intermediate Calculation
Mass = k.Eout * (1 / i.nTurbine)
Mass = Mass / (k.g * waterHead - (i.totalPipes - i.nPipe) * (frictionLossDown + bendLossDown))

# Calculate surface area of reservoir
area = (Mass / k.density) / (i.dWater - i.dPipe)

# Calculate Ein
Ein = Mass / i.nPump
Ein = Ein * (k.g * waterHead + (i.totalPipes - i.nPipe) * (bendLossUp + frictionLossUp))
Ein = MISC.JoulestoMWH(Ein)

# Calculate efficiency
efficiency = MISC.JoulestoMWH(k.Eout) / Ein

# Calculate fill and drain time
fillTime = MISC.Time(Mass, i.Qpump)
drainTime = MISC.Time(Mass, i.Qturbine)

# Calculate total cost of project
cost = cost.findCost(i.zone, i.nPump, i.Qpump, i.dPipe, i.lPipe, i.fPipe, i.totalPipes, i.dWater, i.hWater, area, i.bendCoefficient, i.nTurbine, i.Qturbine, i.areaUnderPipes)

# Calculate cost per percent efficiency
unitCost = cost / (100 * efficiency)

ins = open("inputs.py", "r")
while (ins.readline().rstrip("\n") != "#BEGIN"): # read in inputs
    pass
for line in ins.readlines():
    output.append(line)

out = open(i.filename + ".txt","a")
out.write("-------------------------------------------------------------------------------\n")
out.write("Inputs:\n")
out.writelines(output)
out.write("\n\nOutput:\n")
out.write("Surface Area (m^2) = " + str(area) + "\n")
out.write("Ein          (MWh) = " + str(Ein) + "\n")
out.write("Efficiency         = " + str(efficiency) + "\n")
out.write("Fill Time  (hours) = " + str(fillTime) + "\n")
out.write("Drain Time (hours) = " + str(drainTime) + "\n")
out.write("Cost          ($)  = " + str(cost) + "\n")
out.write("$ / %Efficiency    = " + str(unitCost))
out.write("\n")

out.close()
ins.close()