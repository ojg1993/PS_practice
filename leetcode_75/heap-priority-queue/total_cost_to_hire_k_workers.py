class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_workers, right_workers = costs[:candidates], costs[max(candidates, len(costs) - candidates) :]
        heapq.heapify(left_workers)
        heapq.heapify(right_workers)
        left, right = candidates, max(candidates, len(costs) - candidates) - 1
        res = 0

        for _ in range(k):
            if not right_workers or (left_workers and left_workers[0] <= right_workers[0]):
                res += heapq.heappop(left_workers)
                if left <= right:
                    heapq.heappush(left_workers, costs[left])
                    left += 1
            else:
                res += heapq.heappop(right_workers)
                if left <= right:
                    heapq.heappush(right_workers, costs[right])
                    right -= 1
        return res
