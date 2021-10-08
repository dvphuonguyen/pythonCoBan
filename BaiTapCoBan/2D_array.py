#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    sum_a = []
    for index in range(0,4):
        for key in range (0,4):
            a = sum(arr[index][key:key+3]) + arr[index + 1][key + 1] + sum(arr[index + 2][key : key + 3])
            sum_a.append(a)

    max_s = sum_a[0]
    for element in sum_a:
        if element > max_s:
            max_s = element
    print(max_s)
