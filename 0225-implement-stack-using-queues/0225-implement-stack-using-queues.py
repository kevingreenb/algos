class Node:
    def __init__(self, val: int, next_node: 'Node' = None):
        self.val = val
        self.next = next_node

class MyStack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        self.head = Node(x, self.head)

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from empty stack")
        val = self.head.val
        self.head = self.head.next
        return val

    def top(self) -> int:
        if self.empty():
            raise IndexError("top from empty stack")
        return self.head.val

    def empty(self) -> bool:
        return self.head is None