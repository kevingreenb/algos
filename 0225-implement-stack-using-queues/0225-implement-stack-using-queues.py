class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None

class MyStack:


    def __init__(self):
        self.tail = Node(0)

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = self.tail.next

    def pop(self) -> int:
        value = self.top()
        self.tail = self.tail.prev
        self.tail.next = None
        return value

    def top(self) -> int:
        return self.tail.val

    def empty(self) -> bool:
        return self.tail.prev is None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()