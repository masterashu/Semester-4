#!/bin/python3
# Python: Increasing List

import math
import os
import random
import re
import sys

# Answer
class IncreasingList:
    def __init__(self):
        self._list = []

    def append(self, val):
        """
        first, it removes all elements from the list that have greater values than val, starting from the last one, and once there are no greater element in the list, it appends val to the end of the list
        """
        self._list = list(filter(lambda x: x<=val, self._list))
        self._list.append(val)

    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise, if the list is empty, it does nothing
        """
        if len(self._list) > 0:
            return self._list.pop(-1)

    def __len__(self):
        """
        returns the number of elements in the list
        """
        return len(self._list)

if __name__ == '__main__':
    lst = IncreasingList()
    q = int(input())
    for _ in range(q):
        op = input().split()
        op_name = op[0]
        if op_name == "append":
            val = int(op[1])
            lst.append(val)
        elif op_name == "pop":
            lst.pop()
        elif op_name == "size":
            print("%d\n" % len(lst))
        else:
            raise ValueError("invalid operation")
