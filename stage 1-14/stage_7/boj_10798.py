# 10798

array = [list(input()) for i in range(5)]


for i in range(15):
    for j in range(5):
        try:
            print(array[j][i], end='')
        except:
            continue