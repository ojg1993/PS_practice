# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = head = ListNode()
        array = []

        for l in lists:
            while l:
                array.append(l.val)
                l = l.next

        for val in sorted(array):
            temp.next = ListNode(val)
            temp = temp.next

        return head.next
