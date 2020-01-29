#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
  length = 1
  for i in range(length, len(s)):
    sequence = s[:i]
    cur_num = int(sequence)
    first_num = cur_num
    while len(sequence) < len(s):
      cur_num += 1
      sequence += str(cur_num)
    if sequence == s:
      print('YES %d' % first_num)
      return
  print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
