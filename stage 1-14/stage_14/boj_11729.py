# 11729

# def hanoi_tower(n, s, e):
#     global cnt
#     if n == 1:
#         print(s, e)
#         return
#     else:
#         hanoi_tower(n-1, s, 6-s-e)
#         print(s, e)
#         hanoi_tower(n-1, 6-s-e, e)


# n = int(input())
# print(2**n-1)
# hanoi_tower(n, 1, 3)

# 11729

def hanoi_tower(n, s, e, o):
    global cnt
    if n == 1:
        print(s, e)
        return
    else:
        hanoi_tower(n-1, s, o, e)
        print(s, e)
        hanoi_tower(n-1, o, e, s)


n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3, 2)