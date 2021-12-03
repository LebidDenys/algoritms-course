class DequeueArray:
    def __init__(self, size):
        self.size = size
        self.front, self.last = -1, size
        self.array = [None] * size

    def insertFront(self, value):
        if self.isFull():
            return False
        else:
            self.front = self.front + 1
            self.array[self.front] = value
            return True

    def insertLast(self, value):
        if self.isFull():
            return False
        else:
            self.last = self.last - 1
            self.array[self.last] = value
            return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        elif self.front == -1 or self.array[self.front] is None:
            return self.deleteLast()
        else:
            self.array[self.front] = None
            self.front = self.front - 1
            return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        elif self.last == self.size or self.array[self.last] is None:
            return self.deleteFront()
        else:
            self.array[self.last] = None
            self.last = self.last + 1
            return True

    def getFront(self):
        if self.isEmpty():
            return -1
        elif self.checkFront():
            return self.getRear()
        else:
            return self.array[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        elif self.checkLast():
            return self.getFront()
        else:
            return self.array[self.last]

    def isFull(self):
        return self.front + 1 == self.last and self.array[self.last] is not None and self.array[self.front] is not None

    def isEmpty(self):
        return self.checkFront() and self.checkLast()

    def checkFront(self):
        return self.front == -1 or self.array[self.front] is None

    def checkLast(self):
        return self.last == self.size or self.array[self.last] is None


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
# print(circularDeque.deleteLast())
# print(circularDeque.getFront())
# print(circularDeque.getFront())
# print(circularDeque.insertLast(74))

# "insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getRear","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
# [74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]

# ["MyCircularDeque","insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull","insertFront","isFull","getRear","deleteLast","getFront","getFront","insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getRear","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
# [[77],[89],[],[],[],[19],[23],[23],[82],[],[45],[],[],[],[],[],[74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]
                                                        #|
# [null,true,89,true,-1,true,true,true,true,false,true,false,45








# circularDeque = DequeueArray(3)
# print(circularDeque.insertFront(9))
# print(circularDeque.getRear())
# print(circularDeque.insertFront(9))
# print(circularDeque.getRear())
# print(circularDeque.insertLast(5))
# print(circularDeque.getFront())
# print(circularDeque.getRear())
# print(circularDeque.getFront())
# print(circularDeque.insertLast(8))
# print(circularDeque.deleteLast())
# print(circularDeque.getFront())
# ["MyCircularDeque","insertFront","getRear","insertFront","getRear","insertLast","getFront","getRear","getFront","insertLast","deleteLast","getFront"]
# [[3],[9],[],[9],[],[5],[],[],[],[8],[],[]]
