# 10799

array = list(input())
stk = []
ans = 0

for i in range(len(array)):
    if array[i] == '(':
        stk.append(array[i])
    else:
        if array[i-1] == '(':
            stk.pop()
            ans += len(stk)
        else:
            stk.pop()
            ans += 1


print(ans)