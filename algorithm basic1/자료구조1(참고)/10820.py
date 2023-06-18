# 10820

while True:
    ans = {'l':0,'c':0,'n':0,'s':0}
    try:
        a = input()
        for i in a:
            if i.islower():
                ans['l'] += 1
            elif i.isupper():
                ans['c'] += 1
            elif i.isdigit():
                ans['n'] += 1
            else:
                ans['s'] += 1
        print(*ans.values())
    except:
        break
