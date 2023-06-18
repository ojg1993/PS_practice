# 10809

import string
q = list(input())
alpha = string.ascii_lowercase
ans = []

for s in alpha:
    if s in q:
        ans.append(q.index(s))
    else:
        ans.append(-1)
        
print(*ans)