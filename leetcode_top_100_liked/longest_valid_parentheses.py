



def long(s):
    max_length = 0
    stk = [-1]

    for i in range(len(s)):
        if s[i] == '(':
            stk.append(i)
        else:
            stk.pop()
            if not stk:
                stk.append(i)
            else:
                max_length = max(max_length, i-stk[-1])
    return max_length

a = input()

print(long(a))