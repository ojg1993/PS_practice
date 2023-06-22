# 1436

n = int(input())
first = 666
cnt = 0

while True:
    if '666' in str(first):
        cnt += 1
    if cnt == n:
        print(first)
        break
    first += 1