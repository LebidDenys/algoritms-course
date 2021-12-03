class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyCircularDeque:
    def __init__(self, size):
        self.front_sentinel = Node(None)
        self.rear_sentinel = Node(None)
        self.front_sentinel.next, self.front_sentinel.prev = self.rear_sentinel, self.rear_sentinel
        self.rear_sentinel.next, self.rear_sentinel.prev = self.front_sentinel, self.front_sentinel
        self.size = size
        self.counter = 0
        self.front, self.rear = self.front_sentinel, self.rear_sentinel

    def isFull(self):
        return self.counter == self.size

    def isEmpty(self):
        return self.counter == 0

    def insertFront(self, value):
        if self.isFull():
            return False
        front_node = Node(value)
        if self.rear.data is None:
            self.rear = front_node
        front_node.next, front_node.prev = self.front, self.front.prev
        self.rear.next, self.front.prev = front_node, front_node
        self.front = front_node
        self.counter = self.counter + 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        last_node = Node(value)
        if self.front.data is None:
            self.front = last_node
        last_node.next, last_node.prev = self.front, self.rear
        self.rear.next, self.front.prev = last_node, last_node
        self.rear = last_node
        self.counter = self.counter + 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front.next.prev, self.rear.next = self.rear, self.front.next
        self.counter = self.counter - 1
        if self.counter == 0:
            self.rear = self.rear_sentinel
            self.front = self.front_sentinel
        self.front = self.front.next
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.front.prev, self.rear.prev.next = self.rear.prev, self.front
        self.counter = self.counter - 1
        if self.counter == 0:
            self.rear = self.rear_sentinel
            self.front = self.front_sentinel
        self.rear = self.rear.prev
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.front.data

    def getRear(self):
        if self.isEmpty():
            return -1
        else:
            return self.rear.data


circularDeque = MyCircularDeque(789)
print(circularDeque.insertFront(332))
print(circularDeque.getRear())
print(circularDeque.insertFront(68))
print(circularDeque.deleteLast())
print(circularDeque.getRear())
print(circularDeque.isFull())
print(circularDeque.getFront())
print(circularDeque.deleteFront())
print(circularDeque.isEmpty())
print(circularDeque.getRear())
print(circularDeque.getFront())
print(circularDeque.getFront())

print(circularDeque.deleteLast())
print(circularDeque.getRear())
print(circularDeque.getRear())
print(circularDeque.getFront())
print(circularDeque.getRear())

print(circularDeque.isEmpty())
print(circularDeque.deleteLast())
print(circularDeque.insertLast(783))
print(circularDeque.getFront())
print(circularDeque.getRear())

# null,true,true,false,true,66,true,false,72,false,true,false,66

# ["MyCircularDeque","insertFront","getRear","insertFront","deleteLast","getRear","isFull"
# ,"getFront","deleteFront","isEmpty","getRear","getFront","getFront",
# "deleteLast","getRear","getRear","getFront","getRear",
# "isEmpty","deleteLast","insertLast","getFront","getRear"
# [[789],[332],[],[68],[],[],[],
# [],[],[],[],[],[],[],[],[],[],[],[],[],[783],[],[]

# null,true,332,true,true,68,false,68,true,true,-1,-1,-1,false,-1,-1,-1,-1,true,false,true,783
