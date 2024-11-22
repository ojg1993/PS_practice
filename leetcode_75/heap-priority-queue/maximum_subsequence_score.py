class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        1, 3, 3, 2  -> 2, 3, 1, 3
        2, 1, 3, 4  -> 4, 3, 2, 1

        heap    = [2] -> [2, 3] -> [1, 2, 3]
        cur_sum = 2 -> 5 -> 6
        n2      = 4 -> 3 -> 2         -> res = 6 * 2 = 12
        ------
        heap    = [2] -> [2, 3] -> [1, 2, 3] -> [1, 2, 3, 3]
        cur_sum = 2 -> 5 -> 6 -> 9
        n2      = 4 -> 3 -> 2 -> 1

        if pop value 1 is removed from heap and decrement cur_sum by 1

        heap    = [2] -> [2, 3] -> [1, 2, 3] -> [1, 2, 3, 3] -> [2, 3, 3]
        cur_sum = 2 -> 5 -> 6 -> 9 -> 8
        n2      = 4 -> 3 -> 2 -> 1

        res = max(12, 8) -> 12
        """
        pairs = [p for p in zip(nums1, nums2)]
        pairs.sort(key=lambda p: -p[1])

        heap = []
        res = cur_sum = 0

        for n1, n2 in pairs:
            cur_sum += n1
            heapq.heappush(heap, n1)

            if len(heap) == k:
                res = max(res, cur_sum * n2)
                cur_sum -= heapq.heappop(heap)
        return res
