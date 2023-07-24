# 1476
import sys

input = sys.stdin.readline

# 코드 최적화
e, s, m = map(int, input().split())
year = 1


while True:
    if not (year-e) % 15 and not (year-s) % 28 and not (year-m) % 19:
        break
    year += 1

print(year)

# 직관적 풀이

# e, s, m = map(int, input().split())
#
# ne, ns, nm = 1, 1, 1
# y = 1
#
# while True:
#     if ne == e and ns == s and nm == m:
#         print(y)
#         break
#     else:
#         ne += 1
#         ns += 1
#         nm += 1
#         y += 1
#         if ne == 16:
#             ne = 1
#         if ns == 29:
#             ns = 1
#         if nm == 20:
#             nm = 1
