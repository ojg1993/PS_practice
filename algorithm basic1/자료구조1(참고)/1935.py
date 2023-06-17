# 1935

n = int(input())
q = input()
dict = {s:int(input()) for s in sorted(list(set(q))) if s.isalpha()}
stk = []

for s in q:
    if s.isalpha():
        stk.append(dict[s])
    else:
        b, a = stk.pop(), stk.pop()
        
        if s == '+':
            stk.append(a + b)
        elif s == '-':
            stk.append(a-b)
        elif s == '*':
            stk.append(a*b)
        else:
            stk.append(a/b)
print('{:.2f}'.format(*stk))