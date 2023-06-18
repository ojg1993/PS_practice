# 10808
import string

q = input()
cases = string.ascii_lowercase
dict = {c:0 for c in cases}

for i in q:
    dict[i] += 1

print(*dict.values())