def permuteList(arr):
  if len(arr) == 0:
    return []
  if len(arr) == 1:
    # mimicking permutations which is a list of lists
    return [arr]

  permutations = []
  for i in range(len(arr)):
    first_value = [arr[i]]
    remainder = arr[:i] + arr[i+1:]

    for p in permuteList(remainder):
      permutations.append(first_value + p)

  return permutations

print(permuteList([1,2,3]))

def permuteString(string):
  if len(string) == 0:
    return ''
  if len(string) == 1:
    return [string]

  permutations = []
  for i in range(len(string)):
    first_letter = string[i]
    remaining_string = string[:i] + string[i+1:]

    for p in permuteString(remaining_string):
      permutations.append(first_letter + p)

  return permutations

print(permuteString('123'))
