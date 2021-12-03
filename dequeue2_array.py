class DequeueArray:
    def __init__(self, size):
        self.size = size
        self.front, self.rear = -1, 0
        self.array = [None] * size

    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or self.front == self.rear + 1

    def isEmpty(self):
        return self.front == -1

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.front == -1:
            self.front, self.rear = 0, 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front = (self.front - 1) % self.size
        self.array[self.front] = value
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.front == -1:
            self.front, self.rear = 0, 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear = self.rear + 1
        self.array[self.rear] = value
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        if self.rear == self.front:
            self.rear, self.front = -1, -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        if self.rear == self.front:
            self.rear, self.front = -1, -1
        else:
            self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.array[self.front]

    def getRear(self):
        if self.isEmpty() or self.rear < 0:
            return -1
        else:
            return self.array[self.rear]


circularDeque = DequeueArray(77)
print(circularDeque.insertFront(89))
print(circularDeque.getRear())
print(circularDeque.deleteLast())
print(circularDeque.getRear())
print(circularDeque.insertFront(19))
print(circularDeque.insertFront(23))
print(circularDeque.insertFront(23))
print(circularDeque.insertFront(82))
print(circularDeque.isFull())
print(circularDeque.insertFront(45))
print(circularDeque.isFull())
print(circularDeque.getRear())

# ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]
# [[3],[1],[2],[3],[4],[],[],[],[4],[]]
# Output
# [null,true,true,true,true,3,false,true,true,4]
# Expected
# [null,true,true,true,false,2,true,true,true,4]