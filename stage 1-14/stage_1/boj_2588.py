a = input()
b = input()

c =0
tot = 0
for i, v in enumerate(b[::-1]):
    c = 0
    c += int(a) * int(v)
    print(c)
    tot += c * (10 ** (i))
print(tot)