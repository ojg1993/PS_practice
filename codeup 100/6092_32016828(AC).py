n = int(input())
a = map(int, input().split())
array = [0] * (23)

for i in a:
  array[i-1] +=1

for i in array:
  print(i, end=' ')
