def genPermutations(arr):
  if len(arr) == 0:
    return []
  if len(arr) == 1:
    return [arr]

  out = []
  for i in range(len(arr)):
    first = arr[i]
    rem = arr[:i] + arr[i+1:]
    for p in genPermutations(rem):
      out.append([first] + p)

  return out

def isMagicSquare(arr):
  # check horizontals
  for i in range(0,7,3):
    if sum(arr[i:i+3]) != 15:
      return False

  # check verticals
  for i in range(0,3):
    val = 0
    for j in range(0,3):
      val += arr[i+3*j]
    if val != 15:
      return False

  # check diagonals
  if sum([arr[0],arr[4],arr[8]]) != 15 or sum([arr[2],arr[4],arr[6]]) != 15:
    return False

  return True

def genMagicSquare():
  nums = []
  for i in range(1,10):
    nums.append(i)

  magic_squares = []
  for s in genPermutations(nums):
    if isMagicSquare(s):
      magic_squares.append(s)

  return magic_squares

print(genMagicSquare())
