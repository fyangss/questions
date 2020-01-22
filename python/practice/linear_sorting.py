def csort(ints):
  counts = []
  out = []
  for _ in range(max(ints)+1):
    counts.append(0)

  for i in range(len(ints)):
    counts[ints[i]] += 1
    out.append(0)

  for i in range(1, len(counts)):
    counts[i] += counts[i-1]

  for i in range(len(ints)):
    out[counts[ints[i]]-1] = ints[i]
    counts[ints[i]] -= 1

  return out

def modified_csort(ints):
  counts = []
  for _ in range(max(ints)+1):
    counts.append(0)

  for i in range(len(ints)):
    counts[ints[i]] += 1

  for i in range(1, len(counts)):
    counts[i] += counts[i-1]

  return counts

def rsort(ints):
  out = []
  copy = ints.copy()
  for _ in ints:
    out.append(0)

  for p in range(1, len(str(max(ints)))+1):
    digits = []
    for i in copy:
      digits.append((i%(10**p))//(10**(p-1)))

    counts = modified_csort(digits)
    for i in copy[::-1]:
      digit = (i%(10**p))//(10**(p-1))
      out[counts[digit] - 1] = i
      counts[digit] -= 1
    copy = out.copy()

  return out

print(rsort([1]))
print(rsort([2,1]))
print(rsort([0,1]))
print(rsort([562346,234,5673,1,839,12,0]))
print(rsort([17,2,43,212,106,750,47,309,4,2,1,17,52,98,67,85,0]))
