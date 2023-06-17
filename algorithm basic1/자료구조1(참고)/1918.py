# 1918

q = input()
stk = []
ans = ''

for i in q:
    if i.isalpha():
        ans += i
    elif i == '(':
        stk.append(i)
        
    elif i == '*' or i == '/':
        while stk and (stk[-1] == '*' or stk[-1]=='/'):
            ans += stk.pop()
        stk.append(i)
    elif i == '+' or i == '-':
        while stk and stk[-1] != '(':
            ans += stk.pop()
        stk.append(i)
    elif i == ')':
        while stk and stk[-1] != '(':
            ans += stk.pop()
        stk.pop()
        
while stk:
    ans += stk.pop()
    
print(ans)