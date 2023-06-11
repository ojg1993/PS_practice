# 1874

cnt = 1
temp = True
stk = []
ans = []

for i in range(int(input())):
    num = int(input())
    while cnt <= num:
        stk.append(cnt)
        ans.append('+')
        cnt += 1
    
    if stk[-1] == num:
        stk.pop()
        ans.append('-')
    else:
        temp = False
        break

if temp:
    for i in ans:
        print(i)
else:
    print('NO')

# 1 ~ n까지 stk append(cnt가 n보다 작거나 같을때만)
# stk[-1]이 n과 같으면 pop
# stk[-1]이 n과 다르면 수열 생성 불가로 temp=False