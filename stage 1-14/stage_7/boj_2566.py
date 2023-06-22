# 2566

array = [list(map(int, input().split())) for i in range(9)]

ans = (0,0,0)

for i in range(9):
    for j in range(9):
        if array[i][j] > ans[0]:
            ans = (array[i][j], i, j)
print(ans[0])
print(ans[1]+1,ans[2]+1)