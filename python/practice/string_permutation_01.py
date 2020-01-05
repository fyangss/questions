def premuteStringHelper(permutation, string_left):
  if len(string_left) == 0:
    print(permutation)
  for i in range(len(string_left)):
    a = permutation + string_left[i]
    premuteStringHelper(a, string_left[:i] + string_left[i+1:])

def permuteString(string):
  premuteStringHelper('', string)

permuteString('ABC')
