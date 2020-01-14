#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
  total = sum(bill)
  ana_total = int((total - bill[k])/2)

  if ana_total == b:
    print('Bon Appetit')
  else:
    print(str(b - ana_total))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

