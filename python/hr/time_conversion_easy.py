#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
  time_of_day = s[len(s)-2:]
  hour = s[:2]
  time = s[2:len(s)-2]
  if time_of_day == 'AM':
    if hour == '12':
      return '00' + time
  else:
    if hour != '12':
      hour = str(int(hour) + 12)
      return hour + time
  return hour + time


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

