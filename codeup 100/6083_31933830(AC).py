r,g,b = map(int, input().split())
iter = 0
for i in range(r):
  for j in range(g):
    for h in range(b):
      print(i, j, h)
      iter += 1
print(iter)
