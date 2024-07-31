# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        1. iterate left-1 times and save the node in left_prev variable
        2. iterate right-left+1 times reversing reversing nodes
        3. connect
          - prev_left.next.next to the next node of the original right node
          - prev_left.next to the beginning of the reversed LL
        """

        dummy = ListNode(0, head)
        left_prev = dummy

        for _ in range(left - 1):
            left_prev = left_prev.next

        cur = left_prev.next
        prev = None
        for _ in range(right - left + 1):
            after = cur.next
            cur.next = prev
            prev, cur = cur, after

        left_prev.next.next = after
        left_prev.next = prev
        return dummy.next
