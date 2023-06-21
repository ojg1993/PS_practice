# 11005

n,b = map(int, input().split())

a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans =''


while n:
    remainder = n % b
    
    if remainder >= 10:
        ans += a[remainder]
    else:
        ans += str(remainder)
    n //= b
    
print(ans[::-1])