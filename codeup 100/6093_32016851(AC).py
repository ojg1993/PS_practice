n = int(input())
a = list(map(int, input().split()))

for _ in a[::-1]:
  print(_, end=' ')
