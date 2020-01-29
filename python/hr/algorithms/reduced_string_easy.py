#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
  out = s
  replaced = True
  while replaced:
    print(out)
    if out == '':
      break
    replaced = False
    i = 0
    while i < len(out)-1:
      if out[i] == out[i+1]:
        out = out[:i] + out[i+2:]
        replaced = True
      else:
        i += 1
  
  if out == '':
    return 'Empty String'
  else:
    return ''.join(out)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
