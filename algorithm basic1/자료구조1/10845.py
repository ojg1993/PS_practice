# 10845

from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

for i in range(int(input())):
    order = input().strip().split()
    try:
        if order[0] == 'push':
            queue.append(int(order[1]))
        elif order[0] == 'pop':
            print(queue.popleft())
        elif order[0] == 'size':
            print(len(queue))
        elif order[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif order[0] == 'front':
            print(queue[0])
        elif order[0] == 'back':
            print(queue[-1])
    except:
        print(-1)