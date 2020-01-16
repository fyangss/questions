if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        cur = [name,score]
        students.append(cur)

scores = set()
for s in students:
  scores.add(s[1])
scores = list(scores)
scores.sort()

second_lowest = []
for s in students:
  if s[1] == scores[1]:
    second_lowest.append(s[0])
second_lowest.sort()

for s in second_lowest:
  print(s)
