# 10809
import string

s = input()
alpha = list(string.ascii_lowercase)

for i in alpha:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')