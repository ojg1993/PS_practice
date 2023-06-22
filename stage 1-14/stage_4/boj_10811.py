# 10811

n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]

for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    temp = basket[a:b+1]
    temp.reverse()
    basket[a:b+1] = temp
    
print(*basket)
