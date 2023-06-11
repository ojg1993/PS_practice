#1406
import sys
input = sys.stdin.readline


# char = input().rstrip('\n')
# cursor = len(char)+1

# for i in range(int(input())):
#     a = input().split()
#     if a[0] == 'L' and cursor > 1:
#         cursor -= 1
#     elif a[0] == 'D' and cursor < len(char)+1:
#         cursor += 1
#     elif a[0] == 'B' and cursor > 1:
#         char = char.replace(char[cursor-2], '')
#         # char = char[:cursor-2] + char[cursor-1:]
#         cursor -= 1
#     elif a[0] == 'P':
#         char = char[:cursor-1] + a[1] + char[cursor-1:]
#         cursor += 1
# print(char)

stk1 = [*input().strip()]
stk2 = []
for i in range(int(input())):
    order = [*input().strip().split()]

    if order[0] == 'L':
        if stk1:
            stk2.append(stk1.pop())
    elif order[0] == 'D':
        if stk2:
            stk1.append(stk2.pop())
    elif order[0] == 'B':
        if stk1:
            stk1.pop()
    elif order[0] == 'P':
        stk1.append(order[1])
        
print(''.join(stk1)+''.join(stk2[::-1]))

# string 자료형을 사용하여 예제를 통과하는 코드를 작성했지만 제출시에는 계속 오류가 났다.
# 계속 고민하다가 list를 사용할 수 있다는 해설에서 아이디어를 얻어 풀었지만,
# 풀면서 list자료형을 이렇게도 활용할 수 있구나... 라는 생각을 하게되는 문제였다.