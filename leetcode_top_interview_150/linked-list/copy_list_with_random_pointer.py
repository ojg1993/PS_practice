"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head
        hashmap = dict()

        cur = head

        while cur:
            node = Node(cur.val)
            hashmap[cur] = node
            cur = cur.next

        for node in hashmap:
            hashmap[node].next = hashmap.get(node.next)
            hashmap[node].random = hashmap.get(node.random)

        return hashmap.get(head)
