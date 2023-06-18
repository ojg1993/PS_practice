#1676

n = int(input())
a = 0
def factorial(n):
    global a
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

a = factorial(n)

cnt = 0

for a in str(a)[::-1]:
    if a == '0':
        cnt+=1
    else:
        break
print(cnt)