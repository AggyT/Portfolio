# Project 2 Bend Loss
# File: BendLoss.py
# Date: December 6 2020
# By: Agathiya Tharun
# atharun
# Natalie Harvey
# harve115
# Matthew Stuber
# mjstuber
# Alyssa Devincenzi 
# adevinc
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
# This program has a function that returns the head loss from
# the bends in the pipe system.
#------------------------------------------------------------
import math

def bendloss (velocity, bend):
	return (bend * math.pow(velocity,2) / 2)