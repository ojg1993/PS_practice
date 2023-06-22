# 1157
from collections import Counter

hash = Counter(input().lower())

c = max(hash.values())
array = []

for k,v in hash.items():
    if v == c:
        array.append((k,c))

if len(array) > 1:
    print('?')
else:
    print(array[0][0].upper())