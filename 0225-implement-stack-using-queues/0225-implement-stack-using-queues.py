class Node:
    def __init__(self, val: int, next_node: 'Node' = None):
        self.val = val
        self.next_node = next_node

class MyStack:

    def __init__(self):
        self.head = None
        

    def push(self, x: int) -> None:
        new_node = Node(x, self.head)
        self.head = new_node

    def pop(self) -> int:
        val = self.head.val
        self.head = self.head.next_node
        return val

    def top(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return self.head is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()