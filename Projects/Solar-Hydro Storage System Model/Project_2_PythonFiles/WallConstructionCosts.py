# Project 2
# File: WallConstructionCosts.py
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
# This module deals with the wall construction costs. zoneDiction contains
# data associated with each individual size which can be accessed as needed by
# the funcitons in this module. 
import math as m

zoneDict = { # contains data for each zone to be used in cost analysis
    
    "1": [150000, .25, 282743, 360000, "2 * m.pi * m.sqrt(area / m.pi)", "4 * m.sqrt(area)"],
    
    "2": [208000, .5, 20000, 25617.37, "3 * m.sqrt(2 * area)", "2 * m.sqrt(m.pow(area / 100, 2) + 10000) + 200"],
    
    "3": [250000, .62, 39760.78, 39760.78, "2 * m.pi * m.sqrt(area / m.pi)", "2 * m.pi * m.sqrt(area / m.pi)"]
} #"zone" [fixed cost, variable cost, optimum area cutoff, max area, optimum perimeter, secondary optimum perimter]


# returns linear cost of the wall / m
def WallUnitCost (depth):
    prices = [30,60,95,135,180,250,340]
    heights = [5,7.5,10,12.5,15,17.5,20]
    
    if depth in heights:
        return prices[heights.index(depth)]
    else: # use linear interpolation
        for x in range(len(heights)):
            if depth > heights[x] and depth < heights[x+1]:
                #print("between",heights[x],"and",heights[x+1])
                y2 = prices[x+1]
                y1 = prices[x]
                x2 = heights[x+1]
                x1 = heights[x]
                M = (y2 - y1) / (x2 - x1)
                return ((M * depth) - y1)
            
def Cost(depth, area, zone): # returns total cost of reservoir + zone fixed costs
    linearCost = WallUnitCost(depth)
    if (area <= zoneDict[str(zone)][2]):
        perimeter = eval(zoneDict[str(zone)][4])
    else:
        perimeter = eval(zoneDict[str(zone)][5])
        
    cost = perimeter * linearCost + zoneDict[str(zone)][0] + zoneDict[str(zone)][1] * area
    return cost