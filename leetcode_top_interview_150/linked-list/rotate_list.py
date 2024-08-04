# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1. find the length of the LL
          - iterate LL
        2. calculate the rotate cnt by modular k by length
          - if k%lenght is 0 return head(rotate not required)
        3. connect the tail to the head
        4. iterate LL from head length - k - 1 times to find new_tail
        5. set new_head to new_tail.next
        6. set new_tail.next to None to break the circle
        """

        if not head or not k or not head.next:
            return head

        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1

        rotate = k % length
        if not rotate:
            return head

        cur.next = head

        new_tail = head
        for _ in range(length - rotate - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
