#!/bin/python3

import math
import os
import random
import re
import sys

def getRanking(scores):
  ranks = []

  prev_score = scores[0]
  ranking = 1
  for s in scores:
    if s != prev_score:
      ranking += 1
      prev_score = s
    ranks.append(ranking)

  return ranks

def binarySearch(start, stop, scores, i, ranks):
  mid = int((start + stop) / 2)
  if i == scores[mid]:
    return ranks[mid]
  elif i < scores[mid]:
    if mid == len(scores) - 1:
      return ranks[mid] + 1
    elif i >= scores[mid + 1]:
      return ranks[mid] + 1
    else:
      return binarySearch(mid + 1, stop, scores, i, ranks)
  else:
    if mid == 0:
      return 1
    elif i < scores[mid - 1]:
      return ranks[mid]
    else:
      return binarySearch(start, mid - 1, scores, i, ranks)

def climbingLeaderboard(scores, alice):
  results = []
  ranks = getRanking(scores)

  index = len(scores)-1
  seen = {}
  for a in alice:
    if a in seen:
      results.append(seen[a])
    else:
      rank = binarySearch(0, index, scores, a, ranks)
      seen[a] = rank
      results.append(rank)

  return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

