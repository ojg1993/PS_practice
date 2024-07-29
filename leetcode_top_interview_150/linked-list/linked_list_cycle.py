# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Two Pointer solution O(n) / O(1)
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # Hashmap solution O(n) / O(n)
        # visit = set()
        # cur = head

        # while cur:
        #     if cur in visit:
        #         return True
        #     visit.add(cur)
        #     cur = cur.next
        # return False
