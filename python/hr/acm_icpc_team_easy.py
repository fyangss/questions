#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
  max_subject = -1
  num_teams = 0
  for i in range(len(topic)-1):
    for j in range(i+1, len(topic)):
      subject = 0
      for k in range(len(topic[i])):
        if topic[i][k] == '1' or topic[j][k] == '1':
          subject += 1
      if subject == max_subject:
        num_teams += 1
      elif subject > max_subject:
        num_teams = 1
        max_subject = subject
  return [max_subject, num_teams]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
