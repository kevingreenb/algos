class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.table = [[] for _ in range(self.key_space)]

    def _hash(self, key: int) -> int:
        return key % self.key_space

    def put(self, key: int, value: int) -> None:
        hashed_key = self._hash(key)
        for i, pair in enumerate(self.table[hashed_key]):
            if key == pair[0]:
                self.table[hashed_key][i] = (key, value)
                return
        self.table[hashed_key].append((key, value))

    def get(self, key: int) -> int:
        hashed_key = self._hash(key)
        for i, pair in enumerate(self.table[hashed_key]):
            if key == pair[0]:
                return self.table[hashed_key][i][1]
        return -1   

    def remove(self, key: int) -> None:
        hashed_key = self._hash(key)
        for i, pair in enumerate(self.table[hashed_key]):
            if key == pair[0]:
                del self.table[hashed_key][i]      


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)