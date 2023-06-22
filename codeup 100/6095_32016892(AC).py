n = int(input())
array = [[0]* 19 for i in range(19)]

for _ in range(n):
  a, b = map(int, input().split())
  array[a-1][b-1] = 1

for i in array:
  for j in i:
    print(j, end=' ')
  print()
