# 2480

a, b, c = map(int, input().split())

if a == b and b == c: # 3개가 같을 경우
    print(10_000 + a * 1_000)
elif (a == b and b !=c): # a와 b가 같고 c가 다를 경우
    print(1_000 + b * 100 )
elif (b == c and a != b): # b와 c가 같고 a가 다를 경우
    print(1_000 + b * 100)
elif (a == c and a != b): # a와 c가 같고 b가 다를 경우
    print(1_000 + a * 100)
else:
    print(max(a,b,c) * 100)