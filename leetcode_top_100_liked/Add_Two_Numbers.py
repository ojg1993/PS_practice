# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head  = ListNode()
        cur = head
        carry = 0

        while (l1 != None) or (l2 != None) or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            tot = l1_val + l2_val + carry
            cur.next = ListNode(tot % 10)  # check !
            carry = tot // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        return head.next