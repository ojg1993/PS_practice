# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. create dummy node pointer head
        2. set prev to dummy and cur to head to save node address
        3. iterate LL while cur is not None
          a. while cur.next is not None and cur val equals cur.next val iterate LL and shift cur to cur.next
          b. if prev.next equals cur after the loop, meaning the cur node is not duplicate,
             shift prev and cur to next, acknowledge pre.next was not duplicate.
          c. otherwise, the cur node had duplicate values and at the last node of the duplicates
            - set prev.next to cur.next
            - shift cur to cur.next
        4. return dummy.next
        """
        dummy = ListNode(None, head)
        prev, cur = dummy, head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            if prev.next == cur:
                prev = prev.next
                cur = cur.next
            else:
                prev.next = cur.next
                cur = cur.next

        return dummy.next
