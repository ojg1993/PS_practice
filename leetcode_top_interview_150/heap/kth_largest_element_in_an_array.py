class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

        # h = []

        # for num in nums:
        #     heapq.heappush(h, num)
        #     if len(h) > k:
        #         heapq.heappop(h)
        # return h[0]
