class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (store negatives)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Step 1: add to max heap
        heapq.heappush(self.small, -num)

        # Step 2: balance ordering
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: balance sizes
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()