# 9506


while True:
    a = int(input())
    divisor = []
    if a == -1:
        break
    else:
        for i in range(1,a):
            if a % i == 0:
                divisor.append(i)
    if sum(divisor) == a:
        print(f"{a} = {' + '.join(map(str, divisor))}")
    else:
        print(f'{a} is NOT perfect.')