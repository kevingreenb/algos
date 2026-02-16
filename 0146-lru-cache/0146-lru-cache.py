class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.store = {}
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        ret = self.store[key]
        self.__remove(key)
        self.__add(key, ret.val)
        return ret.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.__remove(key)
        self.__add(key, value)

    def __add(self, key, value):
        node = Node(key, value)
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.store[key] = node
        if len(self.store) > self.capacity:
            self.__remove(self.tail.prev.key)
            
        
    def __remove(self, key):
        node = self.store[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.store[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)