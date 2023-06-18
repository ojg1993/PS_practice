# 11656

q = input()
lst = []
for i in range(len(q)):
    lst.append(q[i:])
    
lst.sort()
for l in lst:
    print(l)