import math
import os
import random
import re
import sys

def binary_number( numbers):
    new_num = []
    while (numbers > 0):
        new_num.append(numbers%2)
        numbers //= 2
    return new_num
def consecutive(lists):
    count= 1
    counts = []
    for index in range(0, len(lists) - 1):
        if lists[index] == lists[index + 1] and lists[index] == 1:
            count += 1
            counts.append(count)
        elif lists[index] == 1:
            counts.append(count)
            count = 1
    return counts
if __name__ == '__main__':
    numbers = int(input())
    lists = binary_number(numbers)
    print(lists)
    counts = consecutive(lists)
    max_e = lists[0]
    for element in counts:
        if element > max_e:
            max_e = element
    print(max_e)