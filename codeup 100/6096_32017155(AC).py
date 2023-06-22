array = []
for _ in range(19):
  a = list(map(int, input().split()))
  array.append(a)

for i in range(int(input())):
  a,b = map(int, input().split())
  for j in range(19):
    if array[j][b-1] == 0:
      array[j][b-1] = 1
    else:
      array[j][b-1] = 0

    if array[a-1][j] == 0:
      array[a-1][j] = 1
    else:
      array[a-1][j] = 0

for i in array:
  for j in i:
    print(j, end=' ')
  print()
