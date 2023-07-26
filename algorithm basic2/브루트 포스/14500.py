n, m = map(int,input().split())
graph = []
ans = 0

def shape1(i, j): # ㅡ
    if j+3 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3]

def shape2(i, j): # ㅣ
    if i+3 >= n:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j]

def shape3(i, j): # L모양
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1]

def shape4(i, j): # L모양 대칭
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j-1]

def shape5(i, j): # L모양 시계방향 회전
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i-1][j] + graph[i-1][j+1] + graph[i-1][j+2]

def shape6(i, j): # L대칭 시계방향 회전
    if i+1 >= n or j+2 >=m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]

def shape7(i, j): # L 시계방향 회전x2
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1]

def shape8(i, j): # L대칭 시계방향 회전x2
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+2][j]

def shape9(i, j): # L 시계방향 회전x3
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i-1][j+2]

def shape10(i, j): # L대칭 시계방향 회전x3
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+2]

def shape11(i, j): # ㅁ모양
    if i+1 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1]

def shape12(i, j): # 번개모양
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]

def shape13(i, j): # 번개모양 회전
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i-1][j+1] + graph[i-1][j+2]

def shape14(i, j): #번개모양 대칭
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j-1]

def shape15(i, j): #번개모양 대칭 회전
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j+2]

def shape16(i, j): #ㅗ모양
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i-1][j+1] + graph[i][j+2]

def shape17(i, j): #ㅗ모양 회전
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j]

def shape18(i, j): #ㅗ모양 회전x2
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i][j+2]

def shape19(i, j): #ㅗ모양 회전x3
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j]


for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        ans = max(ans, shape1(i,j), shape2(i,j), shape3(i,j), shape4(i,j), shape5(i,j), shape6(i,j), shape7(i,j), shape8(i,j), shape9(i,j),
                  shape10(i,j), shape11(i,j), shape12(i,j), shape13(i,j), shape14(i,j), shape15(i,j), shape16(i,j), shape17(i,j), shape18(i,j), shape19(i,j))

print(ans)


## 1차시도

# def count(b, a, figure):
#     tmp = 0
#     if figure == 'a': #         막대
#         sum = 0
#         if a+4 <= x: # x축 좌->우
#             for i in range(a, a+4):
#                 sum += array[b][i]
#             tmp = sum
#             sum = 0
#         if b+4 <= y: # y축 상->하
#             for i in range(b, b+4):
#                 sum += array[i][a]
#             tmp = max(ans, sum)
#
#     elif figure == 'b': #      정사각형
#         sum = 0
#         if a+2 <= x and b+2 <= y:
#             for i in range(b, b+2): # y축
#                 for j in range(a, a+2): # x축
#                     sum += array[i][j]
#             tmp = sum
#
#     elif figure == 'c':#         ㄱ & ㄴ
#         sum = 0
#         if b+3 <= y and a+2 <= x: # ㄴ자 좌 -> 우
#             for i in range(b, b+3):
#                 sum += array[i][a]
#             sum += array[b+2][a+1]
#             tmp = sum
#             sum = 0
#         if b+3 <= y and a-1 >= 0: # ㄴ자 반전 우 -> 좌  ####
#             for i in range(b, b+3):
#                 sum += array[i][a]
#             sum += array[b+2][a-1]
#             tmp = max(tmp, sum)
#             sum = 0
#         if  b+2 <= y and a+3 <= x: #ㄴ자 시계방향
#             for i in range(a, a+3):
#                 sum += array[b][i]
#             sum += array[b+1][a]
#             tmp = max(tmp, sum)
#             sum = 0
#         if  b+2 <= y and a+3 <= x: #ㄴ자 시계방향 상하 반전
#             for i in range(a, a+3):
#                 sum += array[b+1][i]
#             sum += array[b][a]
#             tmp = max(tmp, sum)
#             sum = 0
#         if  b+2 <= y and a+3 <= x: #ㄴ자 반시계 시계방향
#             for i in range(a, a+3):
#                 sum += array[b+1][i]
#             sum += array[b][a+2]
#             tmp = max(tmp, sum)
#             sum = 0
#         if  b+2 <= y and a+3 <= x: #ㄴ자 반시계 시계방향 상하반전
#             for i in range(a, a+3):
#                 sum += array[b][i]
#             sum += array[b+1][a+2]
#             tmp = max(tmp, sum)
#             sum = 0
#         if a-1 >= 0 and b+3 <= y: # ㄱ자
#             for i in range(b, b+3):
#                 sum += array[i][a]
#             sum += array[b][a-1]
#             tmp = max(tmp, sum)
#             sum = 0
#         if b+3 <= y and a+2 <= x: # ㄱ반전
#             for i in range(b, b+3):
#                 sum += array[i][a]
#             sum += array[b][a+1]
#             tmp = max(tmp, sum)
#
#
#     elif figure == 'd':         # ㄴㄱ
#         sum = 0
#         if b+3 <= y and a+2 <= x: # ㄴㄱ 정자
#             for i in range(b, b+2):
#                 sum += array[i][a]
#             for i in range(b+1, b+3):
#                 sum += array[i][a+1]
#             tmp = sum
#             sum = 0
#         if b+3 <= y and a+2 <= x: # ㄴㄱ 반전
#             for i in range(b+1, b+3):
#                 sum += array[i][a]
#             for i in range(b, b+2):
#                 sum += array[i][a+1]
#             tmp = max(tmp, sum)
#             sum = 0
#         if a+3 <= x and b+2 <= y: # ㄴㄱ 시계방향
#             for i in range(a+1, a+3):
#                 sum += array[b][i]
#             for i in range(a, a+2):
#                 sum += array[b+1][i]
#             tmp = max(tmp, sum)
#             sum = 0
#         if a+3 <= x and b+2 <= y: # ㄴㄱ 시계방향 반전
#             for i in range(a, a+2):
#                 sum += array[b][i]
#             for i in range(a+1, a+3):
#                 sum += array[b+1][i]
#             tmp = max(tmp, sum)
#
#     elif figure == 'e':
#         sum = 0
#         if b+2 <= y and a+3 <= x: # 화살표 정방향
#             for i in range(a, a+3):
#                 sum += array[b][i]
#             sum += array[b+1][a+1]
#             tmp = sum
#             sum=0
#         if b+2 <= y and a+3 <= x: # 화살표 상하반전
#             for i in range(a, a+3):
#                 sum += array[b+1][i]
#             sum += array[b][a+1]
#             tmp = max(tmp, sum)
#             sum=0
#         if b+3 <= y and a+2 <= x: # 화살표 시계방향
#             for i in range(b, b+3):
#                 sum += array[i][a+1]
#             sum += array[b+1][a]
#             tmp = max(tmp, sum)
#             sum=0
#         if b+3 <= y and a+2 <= x: # 화살표 반시계방향
#             for i in range(b, b+3):
#                 sum += array[i][a]
#             sum += array[b+1][a+1]
#             tmp = max(tmp, sum)
#
#     return tmp
#
#
# y, x = map(int,input().split())
# array = [list(map(int, input().split())) for _ in range(y)]
# ans = 0
#
# for i in range(y):
#     for j in range(x):
#         ans = max(ans, count(i, j, 'a'), count(i, j, 'b'), count(i, j, 'c'), count(i, j, 'd'), count(i, j, 'e'))
# print(ans)