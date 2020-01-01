def reverseString():
  """
  Done with slicing and py3.
  Negative number in string indexing starts from the end
    e.g. foo_str[-2] = 'e'
  For indexing, the syntax is start:end:stride all optional
    e.g. foo_str[0:5:2] := 0 to 5 skip everyother char

  Therefore, ::-1 means full string, negative 1 stride
  """
  foo_str = 'abcdef'
  print(foo_str[::-1])

def directMatrixAccess():
  a = [[1,2,3],[4,5,6],[7,8,9]]
  print(a[1][1])

def stringDuplication():
  print('hi'*3)

def sortMutates():
  a = [5,4,3,2,1]
  a.sort()
  print(a)
