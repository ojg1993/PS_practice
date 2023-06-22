# 2884

a, b = map(int, input().split())

hours = [i for i in range(24)]
mins = [i for i in range(60)]

if b - 45 < 0:
    print(hours[a-1], mins[b-45])
else:
    print(hours[a], mins[b-45])