a, b = map(int, input().split())
a, b = bool(a), bool(b)

print((a and not(b)) or (b and not(a)))
