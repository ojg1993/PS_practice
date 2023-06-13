# 10866
import sys
from collections import deque
input = sys.stdin.readline

array = deque()

for i in range(int(input())):
    try:
        order = input().split()
        if order[0] == 'push_front':
            array.appendleft(order[1])
        elif order[0] == 'push_back':
            array.append(order[1])
        elif order[0] == 'pop_front':
            print(array.popleft())
        elif order[0] == 'pop_back':
            print(array.pop())
        elif order[0] == 'size':
            print(len(array))
        elif order[0] == 'empty':
            if array:
                print(0)
            else:
                print(1)
        elif order[0] == 'front':
            print(array[0])
        elif order[0] == 'back':
            print(array[-1])
    except:
        print(-1)