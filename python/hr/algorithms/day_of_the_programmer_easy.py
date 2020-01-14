#!/bin/python3

import math
import os
import random
import re
import sys

def leapYear(gregorian, year):
  if gregorian:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
  else:
    return year % 4 == 0

def dayOfProgrammer(year):
  gregorian = year > 1918
  leap_year = leapYear(gregorian, year)
  month_year = '.09.' + str(year)
  day = 13

  if leap_year:
    day -= 1

  if year == 1918:
    return '26.09.1918'
  else:
    return str(day) + month_year


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

