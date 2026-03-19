class MyHashSet:

    def __init__(self):
        self.key_space = 2069
        self.buckets = [[] for _ in range(self.key_space)]

    def _hash(self, key: int) -> int:
        return key % self.key_space

    def add(self, key: int) -> None:
        if not self.contains(key):
            hashed_key = self._hash(key)
            self.buckets[hashed_key].append(key)

    def remove(self, key: int) -> None:
         if self.contains(key):
            hashed_key = self._hash(key)
            self.buckets[hashed_key].remove(key)       

    def contains(self, key: int) -> bool:
        hashed_key = self._hash(key)
        return key in self.buckets[hashed_key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)