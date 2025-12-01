class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.store:
            return ans
        left, right = 0, len(self.store[key])-1
        while left <= right:
            mid = (right+left)//2
            if self.store[key][mid][0] <= timestamp:
                ans = self.store[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
