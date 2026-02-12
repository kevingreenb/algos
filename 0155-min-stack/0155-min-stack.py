class Node:
    def __init__(self, min, val, next = None):
        self.min = min
        self.val = val
        self.next = next

class MinStack:

    def __init__(self):
        self.stack = None
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack = Node(val, val)
        else:
            new_min = min(self.stack.min, val)
            new_node = Node(new_min, val, self.stack)
            self.stack = new_node

    def pop(self) -> None:
        self.stack = self.stack.next

    def top(self) -> int:
        return self.stack.val

    def getMin(self) -> int:
        return self.stack.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()