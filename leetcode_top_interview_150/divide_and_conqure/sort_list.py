# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find middle
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s.next
        s.next = None

        # Recursively devide nodes
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge
        dummy = ListNode(None)
        cur = dummy

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next
