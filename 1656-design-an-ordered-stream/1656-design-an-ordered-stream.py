class OrderedStream:

    def __init__(self, n: int):
        self.store = [None] * (n + 1)
        self.ptr = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey] = value
        results = []
        while self.ptr < len(self.store) and self.store[self.ptr] is not None:
            results.append(self.store[self.ptr])
            self.ptr += 1
        return results
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)