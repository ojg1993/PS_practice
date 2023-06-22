# 5073

# while True:
#     x, y, z = map(int, input().split())
#     if not x:
#         break
    
#     elif x == y and y == z:
#         print('Equilateral')
#     elif (x == y and y != z) or (x != y and y == z) or (x != y and x == z):
#         if max(x,y,z) < ((x+y+z) - (max(x,y,z))):
#             print('Isosceles')
#         else:
#             print('Invalid')
#     elif x != y and y != z and x != z:
#         if max(x,y,z) < ((x+y+z) - (max(x,y,z))):
#             print('Scalene ')
#         else:
#             print('Invalid')
            
while True:
    x, y, z = map(int, input().split())
    if not x:
        break
    
    if x == y == z:
        print('Equilateral')
    elif max(x,y,z) >= ((x+y+z) - max(x,y,z)):
        print('Invalid')
    elif x == y or y == z or x == z:
        print('Isosceles')
    else:
        print('Scalene')