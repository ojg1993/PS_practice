class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.h = set()
        self.n = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.h.remove(smallest)
            return smallest
        self.n += 1
        return self.n - 1

    def addBack(self, num: int) -> None:
        if num < self.n and num not in self.h:
            heapq.heappush(self.heap, num)
            self.h.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
