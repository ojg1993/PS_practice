# 4779

def canto(n, i, j):
    if not n:
        return
    cnt = (j - i +1) // 3
    
    canto(n-1, i, i+cnt-1)
    
    for k in range(i+cnt, i+cnt *2):
        answer[k] = ' '
    
    canto(n-1, i+cnt*2, i+cnt*3-1)

while True:
    try:
        n = int(input())
        answer = ['-'] * (3**n)
        canto(n, 0 , 3**n-1)
        print(''.join(answer))
    except:
        break