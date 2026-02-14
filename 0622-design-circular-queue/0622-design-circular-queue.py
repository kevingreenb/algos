class MyCircularQueue:

    def __init__(self, k: int):
        self.storage = [0] * k
        self.front = 0
        self.rear = -1
        self.stored = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.storage[self.rear] = value
        self.stored += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.stored -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.storage[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.storage[self.rear]

    def isEmpty(self) -> bool:
        return self.stored == 0

    def isFull(self) -> bool:
        return self.stored == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
