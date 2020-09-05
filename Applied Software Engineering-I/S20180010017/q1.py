#!/bin/python3
# Python: List of Even Integers Function

import math
import os
import random
import re
import sys

# Answer 
even = lambda start,n : list(range(start if start % 2 == 0 else start + 1, start+ 2 * n, 2))


if __name__ == '__main__':
    start, n = map(int, input().split())
    res = even(start, n)
    print(" ".join(map(str, res)) + '\n')
    
