#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
  for i in range(n):
    cur_stair = ''
    stairs = i + 1
    for j in range(n-stairs):
      cur_stair += ' '
    for j in range(stairs):
      cur_stair += "#"
    print(cur_stair)

if __name__ == '__main__':
    n = int(input())

    staircase(n)

