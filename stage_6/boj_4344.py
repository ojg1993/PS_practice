# 4344

for _ in range(int(input())):
    a = list(map(int, input().split()))
    tot = sum(a[1:])
    avg = tot / a[0]
    cnt = 0
    for s in a[1:]:
        if s > avg:
            cnt += 1
    print(format(cnt/a[0] * 100, ".3f")+'%')