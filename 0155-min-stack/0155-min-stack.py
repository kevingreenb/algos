class Node:
    def __init__(self, val, min_v, next_node = None):
        self.val = val
        self.min_v = min_v
        self.next = next_node

class MinStack:

    def __init__(self):
        self.head = None
        

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, val)
        else:
            new_node = Node(val, min(val, self.head.min_v), self.head)
            self.head = new_node

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_v


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()