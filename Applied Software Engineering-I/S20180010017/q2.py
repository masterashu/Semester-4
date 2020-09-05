#!/bin/python3
# Python: Return or raise ValueError

import math
import os
import random
import re
import sys

# Answer
def multiply(a, b, bound):
    if a * b > bound:
        raise ValueError(f'multiplication of {a} and {b} with bound {bound} not possible')
    return a * b

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a, b, bound = list(map(int, input().split()))
        try:
            res = multiply(a, b, bound)
            print("%d\n" % res)
        except ValueError as e:
            print("%s\n" % e)

