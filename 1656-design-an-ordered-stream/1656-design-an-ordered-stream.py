class OrderedStream:

    def __init__(self, n: int):
        # Initialize the stream with None; using n+1 for 1-based indexing
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        # Step 1: Insert the value at the specific idKey
        self.stream[idKey] = value
        
        results = []
        
        # Step 2: If the current idKey is where the pointer is, 
        # move the pointer and collect elements
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            results.append(self.stream[self.ptr])
            self.ptr += 1
            
        return results


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)