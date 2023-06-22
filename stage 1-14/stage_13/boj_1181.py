# 1181

arr = []
for _ in range(int(input())):
    word = input()
    arr.append((len(word), word))
    
arr = set(arr)
arr = list(arr)
arr.sort()

for a in arr:
    print(a[1])