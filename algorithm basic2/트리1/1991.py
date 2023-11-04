# 1991
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def preorder(root): # root -> left -> right
    if root.isalpha():
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
def inorder(root): #  left -> root -> right
    if root.isalpha():
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
def postorder(root): #  left -> right -> root
    if root.isalpha():
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


if __name__ == '__main__':
    n = int(input())
    tree = dict()
    for _ in range(n):
        root, left, right = input().split()
        tree[root] = [left, right]

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
