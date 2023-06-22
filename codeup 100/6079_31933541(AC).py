n = int(input())

s = 0
cnt = 1

while True:
    if s < n:
        s += cnt
        cnt += 1
    else:
        print(cnt-1)
        break

    
