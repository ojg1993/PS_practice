# 5086

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    else:
        if not b % a:
            print('factor')
        elif not a % b:
            print('multiple')
        else:
            print('neither')