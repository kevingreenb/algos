class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        node = self.store[key]
        self.__remove(node)
        self.__add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.__remove(self.store[key])
        node = Node(key, value)
        self.__add(node)
        if len(self.store) > self.capacity:
            self.__remove(self.tail.prev)
    
    def __add(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        self.store[node.key] = node

    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        del self.store[node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)