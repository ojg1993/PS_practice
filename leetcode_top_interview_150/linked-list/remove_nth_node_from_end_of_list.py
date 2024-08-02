# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Two pointer approach
          - iterate n time and move fast foward
          - after the iteration, if fast is None return head.next
            -> if fast is None after n times of iteration, n is the first node
          - iterate while fast.next is valid
            - move slow and fast pointer forward
              -> placing the slow node before the removing node using faster node
          - set slow.next to slow.next.next to remove the target node
          - return head
        """
        fast = slow = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
