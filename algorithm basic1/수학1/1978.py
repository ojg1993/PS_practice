# 1978

# bool을 활용한 풀이법
a, b = map(int, input().split())

for i in range(a, b+1):
    c = True
    if i == 1:
        c = False
        continue
    # 에라토스테네스의 체: 2 ~ n의 제곱근까지의 수로 n을 나눌 수 없다면 n은 소수이다.
    for j in range(2, int(i**0.5)+1): 
        if not i % j:
            c=False
            break
    if c:
        print(i)

# for의 else를 활용한 풀이법
a, b = map(int, input().split())

for i in range(a, b+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if not i % j:
            break
    else:
        print(i)