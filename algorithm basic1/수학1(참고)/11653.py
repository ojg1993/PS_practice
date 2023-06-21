# 11653

n = int(input())

while n != 1:
    for i in range(2, n+1):
        if not n%i:
            print(i)
            n //= i
            break