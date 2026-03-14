class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from an empty queue")
        val = self.stack1.pop(0)
        return val

    def peek(self) -> int:
        if self.empty():
            raise IndexError("top from an empty queue")
        return self.stack1[0]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()