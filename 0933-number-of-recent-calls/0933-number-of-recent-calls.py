from collections import deque


class RecentCounter:

    def __init__(self):
        self.list = deque()

    def ping(self, t: int) -> int:
        self.list.append(t)
        while t - self.list[0] > 3000:
            self.list.popleft()
        return len(self.list)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
