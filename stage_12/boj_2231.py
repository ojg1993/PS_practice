# 2231

n = int(input())

tmp = ''
ans = []
for i in range(n):
    tmp = str(i)
    tmp2 = 0
    for j in tmp:
        tmp2 += int(j)
    if (int(tmp) + tmp2) == n:
        ans.append(tmp)

if len(ans):
    print(ans[0])
else:
    print(0)