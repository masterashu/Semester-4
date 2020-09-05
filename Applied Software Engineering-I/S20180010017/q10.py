#!/bin/python3
# Coloring a Grid

import math
import os
import random
import re
import sys

# Theory: Possible unique combinations for single row: 24
# RGB RBG BRG BGR GRB GBR
# RRB RBR BRR BBR BRB RBB
# GGR GRG RGG RRG RGR GRR
# BBG BGB GBB GGB GBG BGG

# Total possible combination : 24^n

# No of cases having one column of same color: 8^n * 3-colors * 3-positions = 9*8^n

# No of cases having two column of same color: 
#       (2^n * 3-colors * 3-positions) when two columns have same color then third column has two choices 
#       + (3^n * 3P2-colors * 3-positions) when two columns have diffrent color then third column has three choices 

# No. of case having all three column of colors => 24

# Using inclusion & exclusion: T(n) = 24^n - 9⁎8^n + 18⁎3^n + 9⁎2^n - 24

# Answer
MOD = int(1e9+7)
def countPatterns(n):
    return (pow(24, n, MOD) 
            - 9 * pow(8, n, MOD) 
            + 18 * pow(3, n, MOD) 
            + 9 * pow(2, n, MOD)
            - 24) % MOD

if __name__ == '__main__':

    n = int(input().strip())

    result = countPatterns(n)

    print(str(result) + '\n')

