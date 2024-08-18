"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        hashmap = {}
        stk = [node]

        # traverse the graph while creating copies of the nodes
        while stk:
            cur = stk.pop()

            if not cur in hashmap:
                hashmap[cur] = Node(cur.val)
                for nei in cur.neighbors:
                    if nei not in hashmap:
                        stk.append(nei)
        # connect new node's neighbours using old nodes's neighbours
        for old, new in hashmap.items():
            for nei in old.neighbors:
                new.neighbors.append(hashmap[nei])
        return hashmap[node]
