#1427
n = input()

arr=[]

for s in n:
    arr.append(s)
arr.sort()
arr.reverse()

print(''.join(arr))