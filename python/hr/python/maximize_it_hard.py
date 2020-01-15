import itertools
# Enter your code here. Read input from STDIN. Print output to STDOUT
km = input().split()
k = int(km[0])
m = int(km[1])
all_a = []
index = []
end = []
for i in range(k):
  arr = list(map(int, input().rstrip().split()))
  all_a.append(arr[1:])
  end.append(len(arr[1:])-1)
  index.append(0)

res = list(itertools.product(*all_a))
s = float('-inf')
for r in res:
  cur_s = 0
  for rr in r:
    cur_s += rr**2
  cur_s = cur_s % m
  s = max(cur_s, s)

print(s)
