w, h, b= map(int, input().split())
g = w * h * b / 8 / 1024 / 1024
print(format(g, '.2f'), 'MB')
