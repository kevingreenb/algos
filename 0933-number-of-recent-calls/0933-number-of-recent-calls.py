from collections import deque

class RecentCounter:
    def __init__(self):
        # Deque is perfect for sliding window problems
        self.queue = deque()

    def ping(self, t: int) -> int:
        # 1. Add the new timestamp
        self.queue.append(t)
        
        # 2. Remove timestamps outside the [t - 3000, t] range
        # This is O(1) on average because each element is added/removed once
        while self.queue[0] < t - 3000:
            self.queue.popleft()
            
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)