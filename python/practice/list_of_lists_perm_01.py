def perm(lists):
  perms = []
  if len(lists) == 0:
    return ''
  if len(lists) == 1:
    for i in lists[0]:
      perms.append([i])
    return perms

  for i in lists[0]:
    for p in perm(lists[1:]):
      perms.append([i] + p)

  return perms

print(perm([[1,2,3],[4,5,6],[7,8,9]]))
