#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
  if isPalindrome(s):
    return -1

  for i in range(len(s)//2):
    if s[i] == s[len(s)-i-1]:
      continue
    else:
      if isPalindrome(s[:i] + s[i+1:]):
        return i
      elif isPalindrome(s[:len(s)-i-1] + s[len(s)-i:]):
        return len(s)-i-1
      else:
        return -1
  
  if s % 2 == 0:
    return -1
  else:
    if isPalindrome(s[:len(s)//2] + s[len(s)//2+1:]):
      return len(s)//2
    else:
      return -1
        

def isPalindrome(s):
  return s == s[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
