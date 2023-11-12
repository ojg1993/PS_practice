# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp  = ListNode()
        cur = temp
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0 # if value is None place 0 to avoid rasing erros
            l2_val = l2.val if l2 else 0
            
            # new digit calculation
            tot = l1_val + l2_val + carry
            cur.next = ListNode(tot % 10)
            carry = tot // 10

            # pointer update
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return temp.next