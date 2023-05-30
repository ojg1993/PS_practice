# 1193

n = int(input())
line =1

while n > line:
    n -= line
    line += 1

if line % 2:
    up = line - n + 1
    down = n
else:
    up = n
    down = line -n + 1

print(up,down, sep='/')