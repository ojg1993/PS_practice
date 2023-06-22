# 10813

a, b = map(int, input().split())

basket = [i for i in range(1,a+1)]
temp = 0
for i in range(b):
    c, d = map(lambda x: int(x) -1, input().split())
    temp = basket[c]
    basket[c] = basket[d]
    basket[d] = temp
print(*basket)

