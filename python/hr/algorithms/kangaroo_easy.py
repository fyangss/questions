#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
  cur_back, cur_front, v_back, v_front = 0,0,0,0
  if x1 < x2:
    if v1 <= v2:
      return 'NO'
    cur_back, cur_front, v_back, v_front = x1,x2,v1,v2
  else:
    if v1 >= v2:
      return 'NO'
    cur_back, cur_front, v_back, v_front = x2,x1,v2,v1

  while cur_back < cur_front:
    cur_back += v_back
    cur_front += v_front
    if cur_back == cur_front:
      return 'YES'
  return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

