# Project 2
# File: costFinder.py
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
# This module accepts design choices, calculates the total cost and returns
# it to the calling function.  
import partsTables as unit
import WallConstructionCosts as wall

grateCost = 0


def findCost(zone, nPump, QPump, dPipe, lPipe, fPipe, tPipes, depth, head, area, bend, nTurbine, QTurbine, pipeArea):      
 
    # price of pump
    cost = QPump * unit.priceLookup(nPump, depth + head, "pump")
    
    
    #price of pipes
    for length in lPipe:
        cost += tPipes * (length * (500 + unit.priceLookup(fPipe, dPipe, "pipe") + pipeArea * 250))
    
    #price of pipe bends
    for b in bend:
        cost += tPipes * unit.priceLookup(b, dPipe, "bend")
        
    #price of wall and other zone costs
    cost += wall.Cost(depth, area, zone)
   
    #price of turbine
    cost += QTurbine * unit.priceLookup(nTurbine, depth + head, "turbine")
    
    #misc extra costs
    cost += grateCost * tPipes
    
    return cost