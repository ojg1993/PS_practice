class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # store index of the nums1 array
        last = m + n - 1

        # iterage and merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        # insert the leftover nums2 in front of nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
