# 11576

a, b = map(int, input().split())
m = int(input())
l = list(map(int, input().split()))
ans = []
tmp = 0

for i in range(len(l)):
    m -= 1
    tmp += l[i]*(a**m)
    
while tmp:
    ans.append(tmp%b)
    tmp //= b
print(*ans[::-1])