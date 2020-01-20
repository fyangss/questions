#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
  cur_time = 1
  counter = 3
  next_start = 6

  while t >= (cur_time + counter):
    cur_time += counter
    counter = next_start
    next_start *= 2
    print(cur_time)
  
  return counter - (t - cur_time)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
