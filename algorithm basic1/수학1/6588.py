# 6588
import sys

r= 1000000
prime = []
primeCheck = [1] * r

for i in range(3, r+1, 2):
    if primeCheck[i]:
        prime.append(i)
        for j in range(2*i, r, i):
            primeCheck[j] = 0

while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    for i in range(len(prime)):
        if primeCheck[n - prime[i]]:
            print(f'{n} = {prime[i]} + {n - prime[i]}')
            break
        
# 일반적인 반복문들을 통해 풀었지만 시간초과가 계속 발생했다.
# 앞에서 배웠던 에라토스테네스의 체로 제곱근을 활용하여 문제를 풀 수 있었지만,
# 실제로 제곱근 이후의 값들이 무조건 1로 초기화 되어 저장된다는게 마음에 들지않아 다른 방법을 계속 찾아보았다.
# 그러던 중 실제로 r까지의 값중 소수들을 체크하고 그 값과 비교하여 정답을 도출해내는 위의 코드까지 도달할 수 있었다.