# 10101

x = int(input())
y = int(input())
z = int(input())

if x + y + z != 180:
    print('Error')
elif x == 60 and y == 60 and z == 60:
    print('Equilateral')
elif x + y + z == 180 and (x==y or y == z or x==z):
    print('Isosceles')
else:
    print('Scalene')
