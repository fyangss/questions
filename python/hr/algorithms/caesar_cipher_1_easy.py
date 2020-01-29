#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
  alpha = 'abcdefghijklmnopqrstuvwxyz'

  out = []
  for i in s:
    if not i.isalpha():
      out.append(i)
      continue
    
    up = False
    if i.isupper():
      up = True
      i = i.lower()

    new = alpha[(ord(i) - ord('a') + k) % 26]
    out.append(new.upper() if up else new)
  return ''.join(out)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
