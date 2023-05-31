# 11653

# n = int(input())
# prime = []

# # 소인수 구하기
# for i in range(2,n+1):
#     if not n % i:
#         for j in range(2, i+1):
#             cnt = 0
#             if not i % j:
#                 cnt += 1
#         if cnt == 1:
#             prime.append(j)
# # 소인수 분해
# while n != 1:
#     for p in prime:
#         if not n % p:
#             n /= p
#             print(p)
#             break

n = int(input())

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n //= i
            break
        
'''
배운점
int 데이터 타입을 '/'로 나누면 몫이 정수로 떨어져도 타입이 float로 저장된다.
처음에 '/'를 사용하고 안되는 이유를 몰라서 방법을 하나씩 구현하여 통과하였지만,
시간이 너무 오래 소요 되어서 '//'를 통해 다시 간단한 방법을 구현했다
'''