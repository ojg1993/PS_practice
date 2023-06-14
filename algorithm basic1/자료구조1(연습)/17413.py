# 17413

# str 사용 풀이
q = input()
idx = 0
ans = ''
word = ''

while idx < len(q):
    if q[idx] == '<':
        while idx < len(q):
            if q[idx] == '>':
                ans += q[idx]
                idx += 1
                break
            else:
                ans += q[idx]
                idx += 1
    else:
        while idx < len(q):
            if q[idx] == ' ':
                ans += word[::-1] + ' '
                idx += 1
                word = ''
                break
            elif q[idx] == '<':
                ans += word[::-1]
                word = ''
                break
            else:
                word += q[idx]
                idx += 1
        ans += word[::-1]

print(ans)

# list 사용 풀이(속도 더 빠름)

word = list(input())
idx = 0
while idx < len(word):
    if word[idx] == '<':
        while word[idx] != '>':
            idx += 1
        idx += 1
    elif word[idx].isalnum():
        s = idx
        while idx < len(word) and word[idx].isalnum():
            idx += 1
        tmp = word[s:idx]
        tmp.reverse()
        word[s:idx] = tmp
    elif word[idx] == ' ': # else 보다 4ms 빠름(negligible)
        idx += 1
print(''.join(word))