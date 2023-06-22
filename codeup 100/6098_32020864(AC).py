array = []
for i in range(10):
  a = list(map(int, input().split()))
  array.append(a)

right = 1
down = 1
array[down][right] = 9

while True:
  if not array[down][right+1]:
    array[down][right+1] = 9
    right += 1
  elif not array[down+1][right]:
    array[down+1][right] = 9
    down +=1
  elif array[down][right+1] == 2:
    array[down][right+1] = 9
    break
  elif array[down+1][right] == 2:
    array[down+1][right] = 9
    break
  else:
    break

for i in array:
  print(*i)
