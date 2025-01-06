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
# This file contians parts tables that the included lookup
# function can access in order to return the cost of a part.
# The first row of the tables represent one design choice, and
# the first column represents a different design choice. It searches
# the indices and uses the intersection of the row and column to
# return the desired part cost.
#------------------------------------------------------------
partDict = {      # Part Catalogue, first row and column represent design choices.
    "pump":      [[  0,  .8, .83, .86, .89, .92],
                  [ 20, 200, 240, 288, 346, 415],
                  [ 30, 220, 264, 317, 380, 456],
                  [ 40, 242, 290, 348, 418, 502],
                  [ 50, 266, 319, 383, 460, 552],
                  [ 60, 293, 351, 422, 506, 607],
                  [ 70, 322, 387, 464, 557, 668],
                  [ 80, 354, 425, 510, 612, 735],
                  [ 90, 390, 468, 561, 673, 808],
                  [100, 429, 514, 617, 741, 889],
                  [110, 472, 566, 679, 815, 978],
                  [120, 519, 622, 747, 896, 1076]],

    "pipe":      [[   0,  .05,  .03,  .02,  .01, .005, .002],
                  [  .1, 1.00,  1.2, 1.44, 2.16, 2.70, 2.97],
                  [ .25, 1.20, 1.44, 1.77, 2.58, 3.23, 3.55],
                  [  .5, 2.57, 3.08, 3.70, 5.55, 6.97, 7.64],
                  [ .75, 6.30, 7.56, 9.07,   14,   17,   19],
                  [   1,   14,   16,   20,   29,   37,   40],
                  [1.25,   26,   31,   37,   55,   69,   76],
                  [ 1.5,   43,   52,   63,   94,  117,  129],
                  [1.75,   68,   82,   98,  148,  185,  203],
                  [   2,  102,  122,  146,  219,  274,  302],
                  [2.25,  144,  173,  208,  311,  389,  428],
                  [ 2.5,  197,  237,  284,  426,  533,  586],
                  [2.75,  262,  315,  378,  567,  708,  779],
                  [   3,  340,  408,  490,  735,  919, 1011]],
     
    "bend":      [[   0,   .1,  .15,  .2,   .22,  .27,   .3],
                  [ 0.1, 1.00, 1.05, 1.10, 1.16, 1.22, 1.28],
                  [0.25, 1.49, 1.57, 1.64, 1.73, 1.81, 1.90],
                  [0.50, 4.93, 5.17, 5.43, 5.70, 5.99,    7],
                  [0.75,   14,   15,   16,   16,   17,   18],
                  [1.00,   32,   34,   36,   38,   39,   41],
                  [1.25,   62,   65,   69,   72,   76,   80],
                  [1.50,  107,  112,  118,  124,  130,  137],
                  [1.75,  169,  178,  187,  196,  206,  216],
                  [2.00,  252,  265,  278,  292,  307,  322],
                  [2.25,  359,  377,  396,  415,  436,  458],
                  [2.50,  492,  516,  542,  569,  598,  628],
                  [2.75,  654,  687,  721,  757,  795,  835],
                  [3.00,  849,  892,  936,  983, 1032, 1084]],
     
    "turbine":      [[    0,  0.83, 0.86, 0.89, 0.92, 0.94],
                     [   20,   360,  432,  518,  622,  746],
                     [   30,   396,  475,  570,  684,  821],
                     [   40,   436,  523,  627,  753,  903],
                     [   50,   479,  575,  690,  828,  994],
                     [   60,   527,  632,  759,  911, 1093],
                     [   70,   580,  696,  835, 1002, 1202],
                     [   80,   638,  765,  918, 1102, 1322],
                     [   90,   702,  842, 1010, 1212, 1455],
                     [  100,   772,  926, 1111, 1333, 1600],
                     [  110,   849, 1019, 1222, 1467, 1760],
                     [  120,   934, 1120, 1345, 1614, 1936]]
}
# Looks up price for part from partDict
# column and row represnt design choices
# kw specifies which part table to acces
def priceLookup(col, row, kw):
    if ((kw == "pump" or kw == "turbine") and row % 10 != 0): # round up height
        while (row % 10 != 0):
            row += 1
        
    col = partDict[kw][0].index(col)
    for element in partDict[kw]:
        if (element[0] == row):
            row = partDict[kw].index(element)
            break
    
    return partDict[kw][row][col]
