# 2250
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''
    문제: n개의 노드로 구성 된 이진트리가 주어질 때, 트리 내 너비가 가장 넓은 레벨과 그 레벨의 넓이 출력
    
    조건
        - 루트노드는 1이 아닐 수 있음
        - 트리는 인접 행렬로 주어짐
        - 각 열에는 1개의 노드만 존재
        - 리프 노드는 -1로 주어짐
        - 레벨 넓이 = (레벨별 우측 끝 노드 - 좌측 끝 노드) + 1
        - 최장 넓이와 같은 넓이를 가진 노드가 존재할 경우 노드의 번호가 작은 노드 우선 출력
        
    세분화 문제
        1. 루트노드 구하기
            -> 루트노드는 타 노드로 부터 참조되지 않으므로, 참조 횟수 기준 탐색
        2. depth 구하기
            -> dfs 활용 max_depth 확인
        3. 입력 노드의 리스트 매핑 [[0]*n for i in range(max_depth)]
            -> 중위 순회, 2차원 리스트 매핑 board[depth, idx] = node
        4. 레벨별 넓이 계산
            -> 리스트.append((노드, 넓이)) -> 넓이 기준 정렬 -> *리스트[0] 출력
'''

def depth_search(root, depth):
    global max_depth
    for next in adj_board[root]:
        if next != -1:
            depth_search(next, depth+1)
            max_depth = max(max_depth, depth+1)
    return max_depth

def inorder_mapping(root, depth):
    global idx
    if int(root) != -1:
        inorder_mapping(adj_board[root][0], depth+1)
        board[depth][idx] = root
        idx += 1
        inorder_mapping(adj_board[root][1], depth+1)

def search_widest_level():
    widths = []
    for level in range(max_depth):
        temp = []
        for node_idx in range(n):
            if board[level][node_idx]:
                temp.append(node_idx)
        widths.append((level+1, temp[-1]-temp[0]+1))
    widths.sort(key=lambda x: x[1], reverse=True)
    return widths[0]

if __name__ == '__main__':
    n = int(input())
    adj_board = {}
    root_node = [0] * (n+1)

    if n == 1:
        print(*[1,1])
        exit()

    for _ in range(n):
        node, left, right = map(int, input().split())
        adj_board[node] = [left, right]
        root_node[node] += 1
        if left != -1: root_node[left] += 1
        if right != -1: root_node[right] += 1
    root_node = root_node.index(1)

    max_depth = 0
    depth_search(root_node, 1) # initializing max depth
    board = [[0]*n for i in range(max_depth)] # board = [0 x n] x max_depth
    idx = 0
    inorder_mapping(root_node, 0) # board mapping by inorder traversal
    print(*search_widest_level())
