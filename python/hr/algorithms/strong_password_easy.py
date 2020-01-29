#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"

  reqs = [len(password), False, False, False, False]

  for i in password:
    if i in numbers:
      reqs[1] = True
    if i in lower_case:
      reqs[2] = True
    if i in upper_case:
      reqs[3] = True
    if i in special_characters:
      reqs[4] = True
  
  missing = 0
  for i in reqs[1:]:
    if not i:
      missing += 1
  
  return max(6-reqs[0], missing)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
