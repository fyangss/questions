from copy import copy

MAGIC_NUM = 15

def checkMagicSquare(arr):
  for i in range(len(arr)):
    horiz_val, vert_val = 0, 0

    for j in range(len(arr)):
      horiz_val += arr[i][j]
      vert_val += arr[j][i]

    if horiz_val != MAGIC_NUM or vert_val != MAGIC_NUM:
      return False

  top_diag, bot_diag = 0, 0
  for i in range(len(arr)):
    top_diag += arr[i][i]
    bot_diag += arr[i][len(arr)-i-1]

  if top_diag != MAGIC_NUM or bot_diag != MAGIC_NUM:
    return False

  return True

def flattenList(list):
  flat_list = []
  for i in list:
    for j in i:
      flat_list.append(j)

  return flat_list

def flatToAry(arr):
  output = []
  cur = []
  for i in range(len(arr)):
    cur.append(arr[i])
    if i % 3 == 2:
      output.append(cur)
      cur = []

  return output

def genMagicSquareHelper(cur_square, nums_left, squares):
  if len(nums_left) == 1:
    cur_list = copy(cur_square)
    cur_list.append(nums_left[0])
    squares.append(cur_list)
  else:
    for i in range(len(nums_left)):
      cur_list = copy(cur_square)
      cur_list.append(nums_left[i])
      genMagicSquareHelper(cur_list, flattenList([nums_left[:i],nums_left[i+1:]]), squares)

def genMagicSquare():
  nums = []
  for i in range(1,10):
    nums.append(i)

  squares = []
  genMagicSquareHelper([], nums, squares)
  for s in squares:
    if checkMagicSquare(flatToAry(s)):
      print(s)

genMagicSquare()
