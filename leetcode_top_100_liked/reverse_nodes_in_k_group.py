# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        pg = dummy

        while True:
            kth = self.get_kth(pg, k)
            if not kth: break
            ng = kth.next

            prev, cur = kth.next, pg.next

            while cur != ng: 
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = pg.next
            pg.next = kth
            pg = tmp

        return dummy.next


    def get_kth(self, node, k):
        while node and k:
            node = node.next
            k -= 1
        return node