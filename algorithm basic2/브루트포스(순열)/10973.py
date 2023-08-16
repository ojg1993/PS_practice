# 10973
import sys
input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if target[i - 1] > target[i]:
        for j in range(n-1, 0, -1):
            if target[i - 1] > target[j]:
                target[i - 1], target[j] = target[j], target[i - 1]
                target = target[:i] + sorted(target[i:],reverse=True)
                print(*target)
                exit()
print(-1)