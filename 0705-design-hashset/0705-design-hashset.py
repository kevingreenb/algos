class MyHashSet:
    def __init__(self):
        self.key_space = 2069
        self.buckets = [[] for _ in range(self.key_space)]

    def _hash(self, key: int) -> int:
        return key % self.key_space

    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        if key not in self.buckets[hash_key]:
            self.buckets[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        if key in self.buckets[hash_key]:
            self.buckets[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self._hash(key)
        return key in self.buckets[hash_key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)