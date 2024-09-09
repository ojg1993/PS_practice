class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res, heap, visit = [], [], set()
        l1, l2 = len(nums1), len(nums2)
        heap.append((nums1[0] + nums2[0], 0, 0))
        visit.add((0, 0))

        while k:
            _, i, j = heapq.heappop(heap)
            res.append((nums1[i], nums2[j]))

            if i + 1 < l1 and (i + 1, j) not in visit:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visit.add((i + 1, j))
            if j + 1 < l2 and (i, j + 1) not in visit:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visit.add((i, j + 1))
            k -= 1
        return res
