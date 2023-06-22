a = int(input())
b = 0 
cnt = 1
while True:
  if b < a:
    b += cnt
    cnt += 1
  else:
    break
print(b)
