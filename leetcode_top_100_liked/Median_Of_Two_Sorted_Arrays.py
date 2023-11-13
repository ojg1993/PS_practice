class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_lst = nums1 + nums2
        merged_lst.sort()
        med = merged_lst[len(merged_lst)//2]

        if len(merged_lst) % 2:
            return float(med)
        else:
            return (med + merged_lst[len(merged_lst)//2 - 1]) / 2