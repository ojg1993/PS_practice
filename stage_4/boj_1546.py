# 1546

a = int(input())
b = list(map(int, input().split()))
c = max(b)

for i, v in enumerate(b):
    b[i] = v / c * 100
    
print(sum(b) / a)