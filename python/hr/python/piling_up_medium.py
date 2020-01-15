# Enter your code here. Read input from STDIN. Print output to STDOUT
def stack(cubes):
  left = 0
  right = len(cubes) - 1
  cur_w = max(cubes[left], cubes[right])
  cur_cubes = 0
  while cur_cubes < len(cubes):
    if max(cubes[left], cubes[right]) > cur_w:
      return False
    if cubes[left] >= cubes[right]:
      cur_w = cubes[left]
      left += 1
    else:
      cur_w = cubes[right]
      right -= 1
    cur_cubes += 1
  return True

n = int(input())
for i in range(n):
  input()
  a = list(map(int, input().rstrip().split()))
  s = stack(a)
  print('Yes' if s else 'No')
