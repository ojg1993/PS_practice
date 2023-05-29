# 2738

n, m = map(int, input().split())

array1 = []
array2 = []

for i in range(n):
    b = list(map(int, input().split()))
    array1.append(b)
    
for i in range(n):
    b = list(map(int, input().split()))
    array2.append(b)

for i in range(n):
    for j in range(m):
        print(array1[i][j] + array2[i][j], end=' ')
    print()