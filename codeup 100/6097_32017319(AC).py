a, b = map(int, input().split())
array = [[0]*b for i in range(a)]

for i in range(int(input())):
  a,b,c,d = map(int, input().split())
  if b:
    for bar in range(a):
      array[c-1+bar][d-1] = 1
  else:
    for bar in range(a):
      array[c-1][d-1+bar] = 1

for i in array:
  for j in i:
    print(j, end=' ')
  print()
