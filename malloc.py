class Node:
	def __init__(self, start, end, is_busy):
		self.start, self.end, self.is_busy = start, end, is_busy
		self.next = None
		self.prev = None


class DoubleLinkedList:
	def __init__(self):
		self.sentinel = Node(0, None, False)
		self.sentinel.next, self.sentinel.prev = self.sentinel, self.sentinel

	def insert_first(self, end, is_busy):
		new_node = Node(self.sentinel.next.start, end - 1, is_busy)
		new_node.next = self.sentinel.next
		new_node.prev = self.sentinel
		self.sentinel.next = new_node
		return new_node

	def insert_last(self, start, end, is_busy):
		new_node = Node(start, end - 1, is_busy)
		new_node.next = self.sentinel
		new_node.prev = self.sentinel.prev
		self.sentinel.prev = new_node
		return new_node

	def add_busy_section(self, free_section: Node, length) -> Node:
		new_section = Node(free_section.start, free_section.start + length - 1, True)
		new_section.prev, new_section.next = free_section.prev, free_section
		free_section.prev.next = new_section
		if new_section.end == free_section.end:
			# new section took all free section space
			new_section.next = free_section.next
			free_section.next.prev = new_section
		else:
			free_section.prev = new_section
			free_section.start = new_section.end + 1
		return new_section

	def add_free_section(self, free_section) -> Node:
		# left and right sections are free
		if not free_section.prev.is_busy and not free_section.next.is_busy:
			# update values
			free_section.start, free_section.end = free_section.prev.start, free_section.next.end
			# update pointers
			free_section.prev.prev.next, free_section.next.next.prev = free_section, free_section
			free_section.prev, free_section.next = free_section.prev.prev, free_section.next.next
		# only left sections is free
		elif not free_section.prev.is_busy:
			# update values
			free_section.start = free_section.prev.start
			# update pointers
			free_section.prev.next, free_section.next.prev = free_section, free_section
		# only right sections is free
		elif not free_section.prev.is_busy:
			# update values
			free_section.end = free_section.next.end
			# update pointers
			free_section.prev.next, free_section.next.prev = free_section, free_section
		# left and right sections are busy
		else:
			free_section.is_busy = False
		return free_section

class Stack:
	def __init__(self, size):
		self.array: [Node] = [None] * size
		self.top = 0

	def push(self, value):
		self.array[self.top] = value
		self.top = self.top + 1

	def pop(self) -> Node:
		self.top = self.top - 1
		return self.array[self.top]


class Malloc:
	def __init__(self, size):
		self.array: [Node] = [None] * size
		self.sections = DoubleLinkedList()
		initial_section = self.sections.insert_last(0, size, False)
		self.array[0] = initial_section
		self.stack = Stack(size)
		self.stack.push(initial_section)

	def malloc(self, length):
		free_section = self.stack.pop()
		if free_section.end - free_section.start < length - 1:
			self.stack.push(free_section)
			return -1
		else:
			busy_section = self.sections.add_busy_section(free_section, length)
			if busy_section.next is free_section:
				self.stack.push(free_section)
			self.array[busy_section.start] = busy_section
			return busy_section.start

	def free(self, index: int):
		if self.array[index] is None:
			return -1
		else:
			free_section = self.sections.add_free_section(self.array[index])
			self.array[free_section.start] = free_section
			self.stack.push(free_section)
			return 0


malloc = Malloc(14)
print(malloc.malloc(2))
print(malloc.malloc(2))
print(malloc.malloc(3))
print(malloc.malloc(2))
print(malloc.malloc(2))
print(malloc.free(2))
print(malloc.free(7))
print(malloc.malloc(2))
print(malloc.malloc(3))
print(malloc.malloc(1))
print(malloc.malloc(3))
print(malloc.malloc(1))
print(malloc.malloc(3))
