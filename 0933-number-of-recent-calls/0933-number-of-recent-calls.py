import heapq
TIME_RANGE  = 3000

class RecentCounter:

    def __init__(self):
        self.list = []
        

    def ping(self, t: int) -> int:
        while self.list and t - self.list[0] > TIME_RANGE:
            heapq.heappop(self.list)
        heapq.heappush(self.list, t)
        return len(self.list)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)