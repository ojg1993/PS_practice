# 1158

# 인덱스 사용 풀이
n, k = map(int, input().split())
round = [i for i in range(1,n+1)]
ans = []
idx = 0

for i in range(n):
    idx += k -1
    if idx >= len(round):
        idx = idx % len(round)
    ans.append(round.pop(idx))
print(str(ans).replace('[', '<').replace(']', '>'))

# queue 사용 풀이

from collections import deque

n, k = map(int, input().split())
round = deque(i for i in range(1, n+1))
ans = deque()

while round:
    for _ in range(k-1):
        round.append(round.popleft())
    ans.append(round.popleft())

print(str(list(ans)).replace('[', '<').replace(']', '>'))