# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
for i in range(n):
  words.append(input())
freq = {}
the_set = []
for w in words:
  if w in freq:
    freq[w] += 1
  else:
    freq[w] = 1
    the_set.append(w)

print(len(the_set))
freqs = []
for w in the_set:
  freqs.append(freq[w])
print(*freqs, sep=' ')
