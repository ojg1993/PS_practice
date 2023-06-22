# 2525
a, b = map(int, input().split())
c = int(input())

hours = [i for i in range(24)]
mins = [i for i in range(60)]

if b + c < 59: # 현재 분과 소요시간 
    print(hours[a], mins[b+c])
else:
    if a == 23:
        if (b+c)//60 > 1:
            a = hours[(b+c)//60]
        else:
            a = hours[0]
    else:
        a = hours[(a + ((b+c)//60))%24]
    b = mins[(b+c) % 60]
    print(a, b)